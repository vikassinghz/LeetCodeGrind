class Solution:
    def intToRoman(self, num: int) -> str:
        RomanRule = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        Roman = []

        for key, value in RomanRule:
            
            C = num // key

            if C != 0:
                Roman.append(value *C)
            num %= key

        return "".join(Roman)

        