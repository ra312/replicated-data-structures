import unittest

from LWW.Set import Set as lww_set

class Test_LWW_Set(unittest.TestCase):
    def test_set_add_remove(self):
        lww = lww_set()
        lww.add("1")
        print("1")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()