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
if "microservice" != "{{cookiecutter.type}}":
    os.remove(Path('.')/'.github'/'workflows'/'container-publish.yaml')
    os.remove(Path('.')/'src'/'{{cookiecutter.package}}'/'core.py')
    os.remove(Path('.')/'src'/'{{cookiecutter.package}}'/'server.py')
    os.remove(Path('.')/'.dockerignore')
    os.remove(Path('.') / 'docker-compose.yml')
    os.remove(Path('.') / 'DockerFile')
if "package" != "{{cookiecutter.type}}":
    os.remove(Path('.')/'.github'/'workflows'/'package-publish.yaml')

subprocess.call(['git', 'init'])
subprocess.call(['tox', '-e', 'setup_version'])
