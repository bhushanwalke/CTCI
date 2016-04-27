__author__ = "bhushan"

import unittest

def CheckPermutation(string):
    str1, str2 = string[0], string[1]
    if len(str1) == len(str2):
        arr1 = [x for x in str1]
        arr2 = [x for x in str2]
        arr1.sort()
        arr2.sort()
        return ''.join(arr1) == ''.join(arr2)
    return False


class Test(unittest.TestCase):
    dataT = [
        (['abcd', 'bacd']), (['3563476', '7334566']),
        (['wef34f', 'wffe34'])
    ]
    dataF = [
        (['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])
    ]

    def test_CheckPermutation(self):
        for test_string in self.dataT:
            self.assertTrue(CheckPermutation(test_string))

        for test_string in self.dataF:
            self.assertFalse(CheckPermutation(test_string))


if __name__ == "__main__":
    unittest.main()
