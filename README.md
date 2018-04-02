SublimeLinter-golint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-golint.png?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-golint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [golint](https://github.com/golang/lint).
It will be used with files that have the "Go" syntax.

Golint is a tool for improving go code. It is _not_ for catching errors! 
It is probably best to use this linter in combination with another error catching linter, such as [gotype](https://github.com/SublimeLinter/SublimeLinter-gotype).


## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Please make sure that the path to `golint` is available to SublimeLinter. To install, follow the instructions provided by [golint](https://github.com/golang/lint).


## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
