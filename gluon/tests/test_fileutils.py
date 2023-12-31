#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import unittest

from gluon.fileutils import fix_newlines, parse_version


class TestFileUtils(unittest.TestCase):
    def test_parse_version(self):
        # Legacy
        rtn = parse_version("Version 1.99.0 (2011-09-19 08:23:26)")
        self.assertEqual(
            rtn, (1, 99, 0, "dev", datetime.datetime(2011, 9, 19, 8, 23, 26))
        )
        # Semantic
        rtn = parse_version("Version 1.99.0-rc.1+timestamp.2011.09.19.08.23.26")
        self.assertEqual(
            rtn, (1, 99, 0, "rc.1", datetime.datetime(2011, 9, 19, 8, 23, 26))
        )
        # Semantic Stable
        rtn = parse_version("Version 2.9.11-stable+timestamp.2014.09.15.18.31.17")
        self.assertEqual(
            rtn, (2, 9, 11, "stable", datetime.datetime(2014, 9, 15, 18, 31, 17))
        )
        # Semantic Beta
        rtn = parse_version("Version 2.14.1-beta+timestamp.2016.03.21.22.35.26")
        self.assertEqual(
            rtn, (2, 14, 1, "beta", datetime.datetime(2016, 3, 21, 22, 35, 26))
        )

    def test_fix_newlines(self):
        fix_newlines(os.path.dirname(os.path.abspath(__file__)))
