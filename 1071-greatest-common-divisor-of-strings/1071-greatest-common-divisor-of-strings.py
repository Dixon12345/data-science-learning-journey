class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 +str1:
            return ""

        len1 = len(str1)
        len2 = len(str2)

        import math
        gcd_len = math.gcd(len(str1),len(str2))
        result_x = str1[0:gcd_len]
        return result_x
        