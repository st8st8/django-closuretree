# Copyright 2015 Ocado Innovation Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup file for django-closuretree.

See also:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages

setup(
    name='django-closuretree',
    # getting version info from git tags
    use_scm_version = True,
    # (the following will be installed into ./.eggs/)
    setup_requires=['setuptools_scm'],

    # specifying packages to install
    packages=find_packages(),

    # dependencies
    # (the following will be installed into ./.eggs/)
    install_requires=['django >= 2.2'],

    # test
    # (the following will be installed into ./.eggs/)
    tests_require=['django-setuptest >= 0.2'],
    test_suite='setuptest.setuptest.SetupTestSuite',

    # meta data
    author='Mike Bryant',
    author_email='mike.bryant@ocado.com',
    description='Efficient tree-based datastructure for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/ocadotechnology/django-closuretree/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
