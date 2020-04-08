// Python Solution
// class Solution:
//     def twoSum(self, nums: List[int], target: int) -> List[int]:
//         h = {}
//         for i, num in enumerate(nums):
//             n = target - num
//             if n not in h:
//                 h[num] = i
//             else:
//                 return [h[n], i]
//         return []

#include <iostream>
#include <unordered_map>
#include <vector>

typedef std::vector<int> vint;

// Questions:
//    Is the array sorted, can there be duplicated elements, can
//    there be negative elements, can I add the same element
//    together twice to get the answer?
// Assumtions:
//    Not sorted, can be duplicate elements, no negative elements,
// you can not add the same two elemenets together twice.
// Other Solutions:
// Loop through all items, and then loop through all other elements
// and check if those two elements sum to what we are looking for. O(n^2)
// Faster solution is add each element to the hashtable, and then check to
// see if the target - the current value is already in the hashtable O(n)

// Two Sum Solution - O(n) - Fastest possible :)
vint twoSum(const vint &nums, int target) {
    std::unordered_map<int, int> mp;

    for (int i = 0; ; i++) {
        auto it = mp.find(target-nums[i]);

        if (it != mp.end())
            return vint{i, it->second};

        mp[nums[i]] = i;
    }
}

int main() {
    vint input = vint{1, 3, 4, 5, 6, 1, 5};
    vint output = twoSum(input, 7);

    for (auto i = 0; output.size(); i++) {
        std::cout << output.at(i) << std::endl;
    }

    return 0;
}
