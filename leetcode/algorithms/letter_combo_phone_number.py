class Solution:
    def letterCombinations(self, digits: str):
        length = len(digits)
        if length == 0:
            return []

        possible = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        digits = digits.replace("1", "1")
        digits = digits[::-1]
        combinations = possible[digits[0]]

        for i in range(1, length):
            iterations = []
            for eachAlpha in possible[digits[i]]:
                [iterations.append(eachAlpha + x) for x in combinations]
            combinations = iterations
        return combinations

        # if len(digits) == 1:
        #     char_arr = possible.get(digits[0])
        #     for char in char_arr:
        #         output.append(char)
        #     return output
        # for i, digit in enumerate(digits):
        #     first_char_arr = possible.get(digit)
        #     for char in first_char_arr:
        #         if i + 1 < len(digits):
        #             next_char_arr = possible.get(digits[i + 1])
        #             for char2 in next_char_arr:
        #                 output.append(char + char2)
