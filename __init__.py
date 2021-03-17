#!/usr/bin/env python

from __future__ import absolute_import
import sys

from pbr.version import VersionInfo

_v = VersionInfo('Algebra_Allen').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

__author__ = "Ousama Dahbi Sebbaghi"
__copyright__ = "Copyright 2021-, Ousama Dahbi Sebbaghi"
__status__ = "Alpha"
__all__ = ('Algebra_Allen')

if sys.hexversion < 0x02050000:
    sys.exit("Python 2.5 or newer is required by tendo module.")
