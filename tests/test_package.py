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
    context = {'project_slug': 'testpackage', 'type': 'package'}
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
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'src')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'src', 'testpackage')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'src', 'testpackage', '__init__.py')))
        self.assertFalse(os.path.exists(os.path.join('testpackage', 'src', 'testpackage', 'core.py')))
        self.assertFalse(os.path.exists(os.path.join('testpackage', 'src', 'testpackage', 'server.py')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'requirements.txt')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'setup.cfg')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'setup.py')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tox.ini')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.gitignore')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'README.rst')))
        self.assertFalse(os.path.exists(os.path.join('testpackage', '.github', 'workflows', 'container-publish.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'workflows', 'lint-test.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'workflows', 'package-publish.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'workflows', 'pr-labeler.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'workflows', 'release-management.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'workflows', 'test-build.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'pr-labeler.yaml')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.github', 'release-drafter.yml')))
        self.assertFalse(os.path.exists(os.path.join('testservice', 'DockerFile')))
        self.assertFalse(os.path.exists(os.path.join('testservice', '.dockerignore')))
        self.assertFalse(os.path.exists(os.path.join('testservice', 'docker-compose.yml')))

    def test_versioneer(self):
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'versioneer.py')))
        os.chdir('testpackage')
        self.assertEqual(subprocess.check_output(['python', 'setup.py', '--version']).decode().rstrip(), '0+unknown')
        os.chdir('..')

    def test_git(self):
        self.assertTrue(os.path.exists(os.path.join('testpackage', '.git')))

    def test_develop(self):
        os.chdir('testpackage')
        self.assertFalse(os.path.exists('.venv'))
        subprocess.check_call(['tox', '-e', 'develop'])
        self.assertTrue(os.path.exists('.venv'))
        os.chdir('..')

    def test_docs(self):
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', 'conf.py')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', 'index.rst')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', '_static')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', '_static', 'custom_manual.cls')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', '_static', 'style.css')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', '_templates')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', '_templates', 'layout.html')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', 'figures')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'docs', 'source', 'figures', '.cookiecutterkeep')))

    def test_tests(self):
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests', 'unit')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests', 'unit', '.cookiecutterkeep')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests', 'functional')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests', 'functional', '.cookiecutterkeep')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests', 'integration')))
        self.assertTrue(os.path.exists(os.path.join('testpackage', 'tests', 'integration', '.cookiecutterkeep')))


class ToxTestCase(unittest.TestCase):
    # Lets test that the build commands are working
    pass
