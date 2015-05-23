from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='m1_gestionsalles_uml',
    version=find_version('m1_gestionsalles_uml', '__init__.py'),
    url='http://github.com/jeremate/m1_gestionsalles_uml/',
    license='GNU GENERAL PUBLIC LICENSE',
    author='Jeremy Klauer and Paul-Jakez Boceno',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='jeremy.klauer@gmail.com',
    description='Projet de gestion de salles développé en Python',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'main = m1_gestionsalles_uml.main:main',
            ],
        # 'gui_scripts': [],
        },
    packages=find_packages(),
    # include_package_data=True,
    # platforms='any',
    # test_suite='sandman.test.test_sandman',
    # zip_safe=False,
    # package_data={'sandman': ['templates/**', 'static/*/*']},
    # classifiers = [
    #     'Programming Language :: Python',
    #     'Development Status :: 4 - Beta',
    #     'Natural Language :: English',
    #     'Environment :: Web Environment',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: Apache Software License',
    #     'Operating System :: OS Independent',
    #     'Topic :: Software Development :: Libraries :: Python Modules',
    #     'Topic :: Software Development :: Libraries :: Application Frameworks',
    #     'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    #     ],
    extras_require={
        'testing': ['pytest'],
      }
)