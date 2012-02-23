'task class'
from __future__ import print_function

class Task(object):
    def __init__(self, **kwargs):
        'initialize defaults'
        self.command = kwargs.pop('command')

        self.watch = kwargs.pop('watch', r'.+\.py')
        self.transform = kwargs.pop('transform', '%s')
        self.transform_command = kwargs.pop('transform_command', None)

        self.success = kwargs.pop('success', None)
        self.failure = kwargs.pop('failure', None)

        self.listen = kwargs.pop('listen', 'all')
        self.ignore = kwargs.pop('ignore', 'none')

        if len(kwargs) > 0:
            print('The following options are ignored/not implemented: %s' % (
                ', '.join(kwargs.keys())
            ))
