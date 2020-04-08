#include <iostream>
#include <algorithm>

// Display array
void display(int a[], int n) {
    for (int i = 0; i < n; i++) {
        std::cout << a[i] << " ";
    }

    std::cout << std::endl;
}

// Find permutations
void findPermutations(int a[], int n) {
    // Sort the given array
    std::sort(a, a+n);

    std::cout << "Possible permutation are:\n";
    do {
        display(a, n);
    } while(std::next_permutation(a, a+n));
}

// Driver code
int main() {
    int a[] = { 10, 20, 30, 40, 50 };

    int n = sizeof(a) / sizeof(a[0]);

    findPermutations(a, n);

    return 0;
}
