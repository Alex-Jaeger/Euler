
#include "problem_0001.hpp"

#include <iostream>

int
euler::problem_0001::getSumOf35Multiples (
    int maximum
) {
    int sum = 0;

    for (int i = 0; i < maximum; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }

    return sum;
}


void
euler::problem_0001::solver () {
    int sumBelow1000 = getSumOf35Multiples(1000);
    std::cout << "Problem 0001 Solution: " << sumBelow1000 << std::endl;
}
