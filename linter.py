from SublimeLinter.lint import util, Linter, WARNING

# Modified Golint linter with extra option "ignores"
# will let to switch off individual linters from
# golint utility.
#
# For instance, if you write Cgo-code to connect to
# API based on C-code, there will be probably a lot of
# "ALL CAPS" constants, which should be reflected
# in same form in Golang. So, such config in
# Preferences->Package Settings->SublimeLinter->Settings
# will supress "ALL CAPS" golint warnings such as
# "gocode.go:50:2: don't use ALL_CAPS in Go names; use CamelCase":
#
#   "linters": {
#       // The name of the linter you installed
#       "golint": {
#           "ignores": {
#               "ALL_CAPS": "1",
#           },
#       },
#   },

class Golint(Linter):
    cmd = 'golint'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'go'
    error_stream = util.STREAM_STDOUT
    default_type = WARNING
    defaults = {
        'selector': 'source.go'
    }

    def split_match(self, match):
        """Process each match modifying or discarding it."""
        match, line, col, error, warning, message, near = super().split_match(match)
        #logger.info(message)
        ignores = self._inline_setting('ignores')
        # find that "ignores" option is defined
        if ignores:
            # support case when "ignores" declared as
            # a JSON object: "ignores": { "ALL_CAPS": "1" }
            # use "1", "True", "true" as a flag to activate option
            if isinstance(ignores, dict):
                for key, value in ignores.items():
                    if isinstance(value, int) and value != 0 or \
                        str(value).upper() in ('1', 'TRUE'):
                        if message and message.find(key) != -1 or \
                            error and error.find(key) != -1 or \
                            warning and warning.find(key) != -1:
                            return None, None, None, None, None, '', None
            # support case when "ignores" declared as
            # a JSON array: "ignores": [ "ALL_CAPS" ]
            elif isinstance(ignores, list):
                for item in ignores:
                    if message and message.find(item) != -1 or \
                        error and error.find(item) != -1 or \
                        warning and warning.find(item) != -1:
                        return None, None, None, None, None, '', None                
        return match, line, col, error, warning, message, near


    def _inline_setting(self, s):
        """Get an inline setting as a bool."""
        setting = self.get_view_settings().get(s)
        return setting
