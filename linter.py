#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell and Jeremy Jay
# Copyright (c) 2014 Jon Surrell
#
# License: MIT
#

"""This module exports the Golint plugin class."""

from SublimeLinter.lint import Linter, util, highlight, persist
import os


class Golint(Linter):

    """Provides an interface to golint."""

    syntax = ('go', 'gosublime-go')
    cmd = 'golint'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDOUT
    default_type = highlight.WARNING

    def find_gopaths(self):
        """search for potential GOPATHs."""
        # collect existing Go path info
        goroot = set(os.path.normpath(s) for s in os.environ.get('GOROOT', '').split(os.pathsep))
        gopath = set(os.path.normpath(s) for s in os.environ.get('GOPATH', '').split(os.pathsep))
        if '.' in gopath:
            gopath.remove('.')
        gopath = list(gopath)

        # search for potential GOPATHs upstream from filename
        # (reversed to ensure deepest path is first searched)
        dirparts = os.path.dirname(self.filename).split(os.sep)
        for i in range(len(dirparts) - 1, 1, -1):
            if dirparts[i].lower() != "src":
                continue
            p = os.path.normpath(os.sep.join(dirparts[:i]))
            if p not in goroot and p not in gopath:
                gopath.append(p)

        if persist.debug_mode():
            persist.printf("{}: {} {}".format(self.name,
                                              os.path.basename(self.filename or '<unsaved>'),
                                              "guessed GOPATH=" + os.pathsep.join(gopath)))

        return os.pathsep.join(gopath)

    def run(self, cmd, code):
        """transparently add potential GOPATHs before running."""
        self.env = {'GOPATH': self.find_gopaths()}

        # copy debug output from Linter.run()
        if persist.debug_mode():
            persist.printf('{}: {} {}'.format(self.name,
                                              os.path.basename(self.filename or '<unsaved>'),
                                              cmd or '<builtin>'))

        return self.tmpfile(cmd, code, suffix=self.get_tempfile_suffix())
