SublimeLinter-golint
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-golint.png?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-golint)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [golint](https://github.com/golang/lint).
It will be used with files that have the "Go" syntax.

This linter plugin has an extra option "ignores", which let to remove individual linters from golint utility.

For instance, if you write Cgo-code to connect to API based on C-code, there probably will be a lot of C-style upper case constants, which should be reflected in same form in Golang. So, such config in Preferences->Package Settings->SublimeLinter->Settings will supress "ALL CAPS" golint warnings such as "gocode.go:50:2: don't use ALL_CAPS in Go names; use CamelCase":
```javascript
  "linters": {
    // The name of the linter you installed
    "golint": {
      // Specify text matches to suppress individual linters from golint output
      "ignores": {
        "ALL_CAPS": true,
      },
    },
  },
 ```

Golint is a tool for improving go code. It is _not_ for catching errors! 
It is probably best to use this linter in combination with another error catching linter, such as [gotype](https://github.com/SublimeLinter/SublimeLinter-gotype).


## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Please make sure that the path to `golint` is available to SublimeLinter. To install, follow the instructions provided by [golint](https://github.com/golang/lint).


## Settings
- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html
