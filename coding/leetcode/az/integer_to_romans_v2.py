from bisect import bisect_right

class Solution:
    def intToRoman(self, num: int) -> str:

        list_M = ["", "M", "MM", "MMM"]
        list_C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        list_X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        list_I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return list_M[num//1000] + list_C[(num%1000)//100] +\
               list_X[(num%100)//10] + list_I[num%10]