"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import unittest
import os
def check_test(self):
    with open(r"C:\Users\lrajan\Desktop\project\PythonBasics\practice\2_python_part_2\task_read_write_2.py","w+") as f:
        f.write("12,11,10,19,18")
        result=f.read()
    self.assertEqual(result,'12,11,10,19,18')
if __name__ == "__main__":
    unittest.main()             