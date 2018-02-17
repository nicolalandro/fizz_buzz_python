import subprocess
import unittest

CORRECT_OUTPUT = "b'1\\n2\\nfizz\\n4\\n5\\nfizz\\n7\\n8\\nfizz\\n10\\n11\\nfizz\\n13\\n14\\nfizz\\n'"


class MyTestCase(unittest.TestCase):
    def test_main(self):
        output = subprocess.check_output(['python', 'src/main.py', '15'])
        self.assertEqual(CORRECT_OUTPUT, str(output))


if __name__ == '__main__':
    unittest.main()
