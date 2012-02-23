'task class'
from __future__ import print_function
import re

class Task(object):
    def __init__(self, **kwargs):
        'initialize defaults'
        self.command = kwargs.pop('command')

        self.watch = kwargs.pop('watch', r'.+\.py')
        self.transform_re = kwargs.pop('transform', '%s')
        self.transform_command = kwargs.pop('transform_command', None)

        self.success = kwargs.pop('success', None)
        self.failure = kwargs.pop('failure', None)

        self.listen = kwargs.pop('listen', 'all')
        self.ignore = kwargs.pop('ignore', 'none')

        if len(kwargs) > 0:
            print('The following options are ignored/not implemented: %s' % (
                ', '.join(kwargs.keys())
            ))

    def match(self, in_str):
        'match a string'
        return re.match(self.watch, in_str)

    def transform(self, match):
        'transform a matched string (SRE_Match object)'
        return match.string
