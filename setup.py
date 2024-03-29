# Copyright 2021 Andrew Rowe.
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

from codecs import open
from setuptools import setup

VERSION = open("VERSION", "r", encoding="utf-8").read().strip()
LONG_DESCRIPTION = open("README.md", "r", encoding="utf-8").read()

setup(
    name="d-serialize",
    version=VERSION,
    description="Universal Python serializer",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Martlark/d_serialize",
    download_url="https://github.com/Martlark/d_serialize/archive/{version}.tar.gz".format(
        version=VERSION
    ),
    author="Andrew Rowe",
    author_email="rowe.andrew.d@gmail.com",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="serialize json convert dict",
    packages=["d_serialize"],
    include_package_data=True,
)
