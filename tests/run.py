import unittest, sys, os
from core import bwt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestRle(unittest.TestCase):
    pass


class TestMtf(unittest.TestCase):
    pass


class TestBwt(unittest.TestCase):
    def testCyclicArray(self):
        self.failIf(bwt.get_cyclic_suffix_array(list('s.t')) != [['s', '.', 't'], ['t', 's', '.'], ['.', 't', 's']])
        self.failIf(bwt.get_cyclic_suffix_array(list('sur')) != [['s', 'u', 'r'], ['r', 's', 'u'], ['u', 'r', 's']])

    def testBwtEncode(self):
        self.failIf(bwt.encode('SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES')[
                        1] != 'TEXYDST.E.IXIXIXXSSMPPS.B..E.S.EUSFXDIIOIIIT')

    def encode_decode(self, string):
        compressed_string = bwt.encode(string)
        recon_str = bwt.decode(compressed_string)
        return string == recon_str

    def test_bwt(self):
        self.failIf(not self.encode_decode('sur'))
        self.failIf(not self.encode_decode('SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES'))


if __name__ == '__main__':
    unittest.main()
