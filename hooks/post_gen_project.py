import subprocess

# run pip install versioneer
# versioneer
subprocess.call(['git', 'init'])
subprocess.call(['tox', '-e', 'setup_version'])
