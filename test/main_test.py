import subprocess
import unittest

import os


class MyTestCase(unittest.TestCase):
    def test_main(self):
        output = subprocess.check_output(['python', '../src/main.py'])
        self.assertEqual("b'ciao\\n'", str(output))


if __name__ == '__main__':
    unittest.main()
