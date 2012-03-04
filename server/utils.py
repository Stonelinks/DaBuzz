import subprocess

def run_bash(cmd):
  p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out = p.stdout.read().strip() + p.stderr.read().strip()
  return out
