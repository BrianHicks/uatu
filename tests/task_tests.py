'tests for uatu/task.py'
import re
from unittest import TestCase

from uatu.task import Task

class MatchTests(TestCase):
    'test Task.match'
    def test_match_default(self):
        task = Task(command='echo')

        in_str = 'test.py'
        expect = re.match('.+\.py', in_str)
        self.assertEqual(expect.string, task.match(in_str).string)

class TransformTests(TestCase):
    'test Task.transform'
    def test_transform_default(self):
        task = Task(command='echo')

        in_str = 'test.py'
        match = re.match('.+\.py', in_str)
        self.assertEqual(in_str, task.transform(match))
