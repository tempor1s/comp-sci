// Python Solution
// class Solution:
//     def fizzBuzz(self, n: int) -> List[str]:
//         res = []
//         for i in range(1, n+1):
//             if i % 3 == 0 and i % 5 == 0:
//                 res.append("FizzBuzz")
//             elif i % 3 == 0:
//                 res.append("Fizz")
//             elif i % 5 == 0:
//                 res.append("Buzz")
//             else:
//                 res.append(str(i))
//         return res

#include <iostream>
#include <vector>

// Questions:
//    Can the number be negative? What is the max
//    size of the number? Can the number be 0?
//
// Assumtions:
//    No negative numbers, max size is the max
// size of an integer, the number can not be 0.
// Other Solutions:
// I can not think of another solution besides the
// one I provided, and the one provided is O(n)
// which I think is the best case for this.

std::vector<std::string> fizzBuzz(int n) {
    std::vector<std::string> output;

    for (int i = 1; i < n + 1; i++) {
        if (i%3 == 0 && i%5 == 0) {
            output.push_back("FizzBuzz");
        } else if (i%3 == 0) {
            output.push_back("Fizz");
        } else if (i%5 == 0) {
            output.push_back("Buzz");
        } else {
            output.push_back(std::to_string(i));
        }
    }

    return output;
}

int main() {
    auto x = fizzBuzz(15);

    for (auto i = 0; i < x.size(); i++) {
        std::cout << x.at(i) << "\n";
    }

    return 0;
}
