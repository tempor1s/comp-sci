class Solution(object):
    """
    Time Complexity:
        Best: O(1) Lenth's do not match or empty str etc
        Average: O(n)
        Worst: O(n)
    """
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in (A + A)
