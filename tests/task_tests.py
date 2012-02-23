'tests for uatu/task.py'
from unittest import TestCase

from uatu.task import Task

class DefaultsTests(TestCase):
    'test defaults'
    def setUp(self):
        'set up a task'
        self.task = Task(command='echo')

    def test_watch(self):
        'watch default'
        self.assertEqual(r'.+\.py', self.task.watch)

    def test_transform(self):
        'transform default'
        self.assertEqual(r'%s', self.task.transform)

    def test_transform_command(self):
        'transform command default'
        self.assertEqual(None, self.task.transform_command)

    def test_success(self):
        'success default'
        self.assertEqual(None, self.task.success)

    def test_failure(self):
        'failure default'
        self.assertEqual(None, self.task.failure)

    def test_listen(self):
        'listen default'
        self.assertEqual('all', self.task.listen)

    def test_ignore(self):
        'ignore default'
        self.assertEqual('none', self.task.ignore)
