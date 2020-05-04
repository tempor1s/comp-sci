class Solution(object):
    """
    Time Complexity:
        Average: O(n+m) Have to loop through both
        Worst: O(n+m) Have to loop through both
    """
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        both, res, min_v = {}, [], float('inf')
        d1 = {v: k for k, v in enumerate(list1)}
        d2 = {v: k for k, v in enumerate(list2)}
        for key in set(d1.keys()).intersection(set(d2.keys())):
            both[key] = d1[key] + d2[key]
            if both[key] < min_v: min_v = both[key]
        for key in both:
            if both[key] == min_v: res.append(key)
        return res
