#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup

PACKAGE_NAME = "py_awesome"

with io.open("%s/__init__.py" % PACKAGE_NAME, "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(version=version)