class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = s.lower()
        newString = "".join(char for char in newString if char.isalnum())
        newString = newString.replace(" ", "")

        left = 0
        right = len(newString) - 1

        while left <= right:
            if newString[left] != newString[right]:
                return False
            left += 1
            right -= 1
        return True
        