"""Offline validation harness; executes original cells without modifying source."""
from pathlib import Path
import argparse,concurrent.futures,contextlib,json,os,subprocess,sys,time,traceback
ROOT=Path(__file__).resolve().parents[1]
RUNS=Path(__file__).resolve().parent/'runs'
RUNS.mkdir(exist_ok=True)
def worker(name):
 import socket,nbformat
 from IPython.display import display
 def offline(*args,**kwargs):raise RuntimeError('Network disabled during validation')
 socket.socket.connect=offline;socket.create_connection=offline
 os.environ.pop('TYPESAFE_API_KEY',None)
 import matplotlib
 matplotlib.use('Agg')
 import matplotlib.pyplot as plt
 plt.show=lambda *a,**k:plt.close('all')
 path=ROOT/name;run=RUNS/path.stem;run.mkdir(exist_ok=True);os.chdir(run)
 nb=nbformat.read(path,as_version=4);nbformat.validate(nb)
 namespace={'__name__':'__main__','display':display};cells=[];start=time.monotonic()
 with (run/'execution.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
  for i,c in enumerate(nb.cells):
   if c.cell_type!='code':continue
   before=time.monotonic();row={'cell_index':i,'status':'PASS'}
   try:exec(compile(c.source,f'{path.name}#cell-{i}','exec'),namespace)
   except BaseException as e:
    row.update(status='FAIL',exception=type(e).__name__,error=str(e));traceback.print_exc()
   row['seconds']=round(time.monotonic()-before,4);cells.append(row)
   (run/'result.json').write_text(json.dumps({'file':name,'cells':cells,'seconds':round(time.monotonic()-start,3)},indent=2))
   if row['status']=='FAIL':return 1
 return 0
def launch(p):
 out=RUNS/p.stem;out.mkdir(exist_ok=True)
 env=dict(os.environ,MPLBACKEND='Agg',MPLCONFIGDIR=str((RUNS/'matplotlib').resolve()),OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
 start=time.monotonic()
 try:
  proc=subprocess.run([sys.executable,__file__,'--worker',p.name],env=env,capture_output=True,text=True,timeout=180)
  r={'file':p.name,'status':'PASS' if proc.returncode==0 else 'FAIL','exit_code':proc.returncode,'seconds':round(time.monotonic()-start,2),'startup_stderr':proc.stderr[-3000:]}
 except subprocess.TimeoutExpired:r={'file':p.name,'status':'TIMEOUT','seconds':180}
 print(json.dumps(r),flush=True);return r
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--worker');args=parser.parse_args()
 if args.worker:sys.exit(worker(args.worker))
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(launch,sorted(ROOT.glob('*.ipynb'))))
 (RUNS/'summary.json').write_text(json.dumps(results,indent=2))
 sys.exit(0 if results and all(r['status']=='PASS' for r in results) else 1)
