SublimeLinter-golint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-golint.png?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-golint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [golint](https://github.com/golang/lint). It will be used with files that have the “Go” syntax.

Golint is a tool for improving go code. It is _not_ for catching errors! It is probably best to use this linter in combination with another error catching linter, such as [gotype](https://github.com/SublimeLinter/SublimeLinter-gotype).


## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `golint` is installed on your system and that its path is available to SublimeLinter. To install, follow the instructions provided by [golint](https://github.com/golang/lint).


## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
