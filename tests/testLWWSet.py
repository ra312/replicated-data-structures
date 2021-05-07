import unittest

from LWW.Set import Set as lww_set

class Test_LWW_Set(unittest.TestCase):
    '''
    tests for LWW-Set
    '''
    def test_set_init(self):
        '''
        test lww-set init 
        '''
        exception_received = False
        try:
            lww = lww_set()
        except:
            exception_received = True
        self.assertFalse(exception_received)


    def test_set_add(self):
        '''
        test adding elements to lww-set
        '''
        lww = lww_set()
        lww.add("1")
        lww.add(1)
    
        self.assertTrue(lww.exists("1"))
        self.assertTrue(lww.exists(1))
    
    def test_set_remove(self):
        '''
            test removing elements from lww-set
        '''
        lww = lww_set()
        lww.add("1")
        try:
            op_state = lww.remove(1)
            # removing non-existent elements is OK?
            self.assertTrue(op_state)
        except Exception as e:
            print(str(e))
        # checking element  has been removed
        # self.assertTrue(not lww.exists("1"))

        lww = lww_set()
        lww.add("1")
        lww.add(1)
        lww.remove("1")
        # checking element  has been removed
        self.assertTrue(not lww.exists("1"))

        lww = lww_set()
        lww.add("1")
        lww.remove("1")
        el_state = lww.exists("1")
        # returns true if element has been either added or removed
        self.assertFalse(el_state)
        

    # def test_set_print(self):
    #     lww = lww_set()
    #     lww.add("1")
    #     lww.add(int(45))
    #     lww.__print__()
    #     self.assertTrue(True)        



if __name__ == '__main__':
    unittest.main()