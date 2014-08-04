#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
long_description = readme
doclink = '''
Documentation
-------------

The full documentation is at http://workbench.rtfd.org. '''
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

exec(open('workbench/server/version.py').read())
setup(
    name='workbench',
    version=__version__,
    description='A scalable framework for security research and development teams.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='The Workbench Team',
    author_email='support@supercowpowers.com',
    url='http://github.com/SuperCowPowers/workbench',
    packages=['workbench_cli', 'workbench', 'workbench.server',
              'workbench.server.bro', 'workbench.workers',
              'workbench.workers.rekall_adapter', 'workbench.clients'],
    package_dir={'workbench': 'workbench', 'workbench_cli': 'workbench_cli/workbench_cli'},
    include_package_data=True,
    scripts=['workbench/server/workbench_server', 'workbench_cli/workbench'],
    tests_require=['tox'],
    install_requires=['cython', 'colorama', 'distorm3>=0', 'elasticsearch',
                      'funcsigs', 'flask', 'filemagic', 'ipython', 'mock', 'pefile',
                      'py2neo', 'pymongo', 'pytest', 'rekall==1.0rc11', 'requests',
                      'ssdeep==2.9-0.3', 'urllib3', 'yara', 'zerorpc', 'cython'],
    license='MIT',
    zip_safe=False,
    keywords='workbench security python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ]
)
