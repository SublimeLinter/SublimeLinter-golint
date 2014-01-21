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
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDOUT
