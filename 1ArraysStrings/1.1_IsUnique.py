# Consider character set is ASCII

import unittest

def IsUnique(string):
    if len(string) > 128:
        return False
    else:
        character_set = [False for x in range(128)]
        for i in string:
            if character_set[ord(i)]:
                return False
            else:
                character_set[ord(i)] = True

        return True


class Test(unittest.TestCase):
    TEST_DATA = [
        ('abcd', True),
        ('s4fad', True),
        ('', True),
        ('23ds2', False),
        ('hb 627jh=j ()', False)
    ]

    def test_IsUnique(self):
        for test_string, result in self.TEST_DATA:
            self.assertEquals(IsUnique(test_string), result)

if __name__ == '__main__':
    unittest.main()

