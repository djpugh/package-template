import os
from pathlib import Path
import shutil
import subprocess

# run pip install versioneer
# versioneer
services = ['package', 'microservice']
for type_ in services:
    if type_ != "{{cookiecutter.type}}":
        os.remove(f'{type_}-requirements.txt')
        os.remove(f'{type_}-tox.ini')
    if type_ == "{{cookiecutter.type}}":
        shutil.move(Path('.')/f'{type_}-requirements.txt', Path('.')/'requirements.txt')
        shutil.move(Path('.')/f'{type_}-tox.ini', Path('.')/'tox.ini')
        shutil.move(Path('.')/'.github'/'workflows'/f'pipeline-{type_}.yml', Path('.')/'.github'/'workflows'/'pipeline.yml')
if "microservice" != "{{cookiecutter.type}}":
    os.remove(Path('.')/'.github'/'workflows'/'pipeline-microservice.yml')
    os.remove(Path('.')/'src'/'{{cookiecutter.package}}'/'core.py')
    os.remove(Path('.')/'src'/'{{cookiecutter.package}}'/'server.py')
    os.remove(Path('.')/'.dockerignore')
    os.remove(Path('.') / 'docker-compose.yml')
    os.remove(Path('.') / 'Dockerfile')
if "package" != "{{cookiecutter.type}}":
    os.remove(Path('.')/'.github'/'workflows'/'pipeline-package.yml')

subprocess.call(['git', 'init'])
subprocess.call(['git', 'checkout', '-b', '{{cookiecutter.main_branch}}'])
subprocess.call(['tox', '-e', 'setup_version'])
