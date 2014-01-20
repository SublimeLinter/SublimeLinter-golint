#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell,,,
# Copyright (c) 2014 Jon Surrell,,,
#
# License: MIT
#

"""This module exports the Golint plugin class."""

from SublimeLinter.lint import Linter, util


class Golint(Linter):

    """Provides an interface to golint."""

    syntax = 'go'
    cmd = 'golint'
    executable = None
    # 001.go:16:19: should drop = 0 from declaration of var result; it is the zero value
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)$'

    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'go'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
