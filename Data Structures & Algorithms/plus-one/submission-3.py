class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            c = digits[i] + carry
            digits[i] = c % 10
            carry = c //10
            if carry == 0:
                return digits
        digits.insert(0,carry)
        return digits