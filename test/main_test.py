import subprocess
import unittest

CORRECT_OUTPUT = "b'1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n10\\n11\\n12\\n13\\n14\\n15\\n'"


class MyTestCase(unittest.TestCase):
    def test_main(self):
        output = subprocess.check_output(['python', 'src/main.py', '15'])
        self.assertEqual(CORRECT_OUTPUT, str(output))


if __name__ == '__main__':
    unittest.main()
