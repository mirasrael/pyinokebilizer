from __future__ import absolute_import, unicode_literals

import os
import unittest
import subprocess


class TestV013Api(unittest.TestCase):
    @staticmethod
    def run_task(*args):
        fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        process = subprocess.Popen(["invoke"] + list(args),
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   cwd=os.path.join(fixtures_dir, 'v0.13'))
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr

    def test_task_without_args(self):
        rc, stdout, stderr = self.run_task('say_hello')
        self.assertEqual(rc, 0, msg=stderr)
        self.assertIn(b'Hello world', stdout)

    def test_task_with_dependencies(self):
        rc, stdout, stderr = self.run_task('greeting')
        self.assertEqual(rc, 0, msg=stderr)
        self.assertIn(b'Hello world', stdout)
        self.assertIn(b'Greeting!', stdout)

    def test_run_all(self):
        rc, stdout, stderr = self.run_task('say_hello_and_say_goodbye')
        self.assertEqual(rc, 0, msg=stderr)
        self.assertIn(b'Hello world', stdout)
        self.assertIn(b'Goodbye', stdout)

    def test_it_reports_nested_failure(self):
        rc, stdout, stderr = self.run_task('say_hello_and_fail')
        self.assertNotEqual(rc, 0, msg="Command should fail")
        self.assertIn(b'Hello world', stdout)
        self.assertIn(b'FAILED TASKS: fail_a, fail_b', stdout)
        self.assertIn(b'FAILED TASKS: fail (fail_a, fail_b)', stdout)

