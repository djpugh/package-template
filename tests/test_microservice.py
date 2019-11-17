import unittest
import tempfile
import os
import shutil
import subprocess

from cookiecutter.main import cookiecutter

TEMPDIR = None
CWD = os.getcwd()
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def setUpModule():
    # create a tempdir
    global TEMPDIR
    global CWD
    TEMPDIR = tempfile.TemporaryDirectory()
    os.chdir(TEMPDIR.name)
    context = {'project_slug': 'testservice', 'type': 'microservice'}
    print(ROOT_DIR)
    cookiecutter(ROOT_DIR, extra_context=context, no_input=True)


def tearDownModule():
    os.chdir(CWD)
    try:
        shutil.remove(TEMPDIR.name)
    except Exception:
        pass


class TemplateTestCase(unittest.TestCase):

    def test_template_structure(self):
        print(TEMPDIR)
        print(CWD)
        self.assertTrue(os.path.exists(os.path.join('testservice', '.ci')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'src')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'src', 'testservice')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'src', 'testservice', '__init__.py')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'src', 'testservice', 'core.py')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'src', 'testservice', 'server.py')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'requirements.txt')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'setup.cfg')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'setup.py')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tox.ini')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.gitignore')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'README.rst')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'workflows', 'container-publish.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'workflows', 'lint-test.yaml')))
        self.assertFalse(os.path.exists(os.path.join('testservice', '.github', 'workflows', 'service-publish.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'workflows', 'pr-labeler.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'workflows', 'release-management.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'workflows', 'test-build.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'pr-labeler.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.github', 'release-drafter.yml')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'DockerFile')))
        self.assertTrue(os.path.exists(os.path.join('testservice', '.dockerignore')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docker-compose.yml')))

    def test_versioneer(self):
        self.assertTrue(os.path.exists(os.path.join('testservice', 'versioneer.py')))
        os.chdir('testservice')
        self.assertEqual(subprocess.check_output(['python', 'setup.py', '--version']).decode().rstrip(), '0+unknown')
        os.chdir('..')

    def test_git(self):
        self.assertTrue(os.path.exists(os.path.join('testservice', '.git')))

    def test_develop(self):
        os.chdir('testservice')
        self.assertFalse(os.path.exists('.venv'))
        subprocess.check_call(['tox', '-e', 'develop'])
        self.assertTrue(os.path.exists('.venv'))
        os.chdir('..')

    def test_docs(self):
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', 'conf.py')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', 'index.rst')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', '_static')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', '_static', 'custom_manual.cls')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', '_static', 'style.css')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', '_templates')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', '_templates', 'layout.html')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', 'figures')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'docs', 'source', 'figures', '.cookiecutterkeep')))

    def test_tests(self):
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests', 'unit')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests', 'unit', '.cookiecutterkeep')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests', 'functional')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests', 'functional', '.cookiecutterkeep')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests', 'integration')))
        self.assertTrue(os.path.exists(os.path.join('testservice', 'tests', 'integration', '.cookiecutterkeep')))


class ToxTestCase(unittest.TestCase):
    # Lets test that the build commands are working
    pass
