# Copyright 2016 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import sys

from setuptools import setup, Extension

libraries = []
if sys.platform == "win32":
    libraries.append("ws2_32")
elif sys.platform != "darwin":
    # librt may be needed for clock_gettime()
    libraries.append("rt")

setup(
    ext_modules=[
        Extension(
            "bsonjs",
            sources=["src/bsonjs.c"] + glob.glob("src/*/*.c"),
            include_dirs=[
                "src",
                "src/bson",
                "src/jsonsl",
                "src/common",
            ],
            define_macros=[
                ("BSON_COMPILATION", 1),
                ("_XOPEN_SOURCE", 700),
                ("Py_LIMITED_API", "0x03070000"),
            ],
            libraries=libraries,
            py_limited_api=True,
        )
    ],
    options={
        "bdist_wheel": {"py_limited_api": "cp37"},
    },
    package_data={
        "bsonjs": ["src/py.typed", "src/*.pyi"],
    },
)
