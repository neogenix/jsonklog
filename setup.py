# -*- coding: utf-8 -*-
#
#   Copyright [2012] [Patrick Ancillotti]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

install_requires = [
        "anyjson",
        ]

setup(name="jsonklog",
    version="0.05",
    description="JSON Logging Library with Python",
    long_description="\n" + README + "\n\n" + CHANGES,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging"
    ],
    license="Apache 2.0",
    author="Patrick Ancillotti",
    author_email="patrick@eefy.net",
    url="http://www.github.com/neogenix/jsonklog",
    keywords="json logging",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['jsonklog'],
    test_suite="",
    install_requires=install_requires,
    entry_points=""" """
)
