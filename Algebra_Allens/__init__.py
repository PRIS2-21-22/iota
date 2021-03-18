#!/usr/bin/env python

from __future__ import absolute_import
import sys

from pbr.version import VersionInfo

_v = VersionInfo('Algebra_Allens').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

__author__ = "Ousama Dahbi Sebbaghi"
__copyright__ = "Copyright 2021-, Ousama Dahbi Sebbaghi"
__email__ = "ods883@inlumine.ual.es"
__status__ = "Alpha"
__all__ = ('Algebra_Allens, __version__')

if sys.hexversion < 0x02050000:
    sys.exit("Python 2.5 or newer is required by tendo module.")
