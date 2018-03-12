
from subprocess import PIPE, run

proc = run('echo works', shell=True, timeout=5, stdout=PIPE, stderr=PIPE)
print (proc.stdout.decode('utf-8'), proc.stderr.decode('utf-8'))

proc = run('sleep 4', shell=True, timeout=2, stdout=PIPE, stderr=PIPE)
print (proc.stdout.decode('utf-8'), proc.stderr.decode('utf-8'))
