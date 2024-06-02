# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup


setup(
    name="visual-acoustic-matching",
    version="0.1.1",
    packages=[
        "vam",
    ],
    install_requires=[],
    extras_require={
        "test": [
            "pylint",
            "pytest",
        ],
    },
)
