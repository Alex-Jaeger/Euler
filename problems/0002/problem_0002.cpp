
#include "problem_0002.hpp"

#include <cmath>
#include <cassert>
#include <iostream>

int
euler::problem_0002::fibonacci (
    int n
) {
    assert(n >= 1);

    float sqrt5 = sqrt(5.0f);
    float inv_sqrt5 = 1.0f / sqrt5;

    return floor(inv_sqrt5 * (powf(((1 + sqrt5) / 2.0), n+1) - powf(((1 - sqrt5) / 2.0), n+1)));
}

int
euler::problem_0002::sumEvenFibonacci (
    int maximum
) {
    int fibIndex = 2;
    int fibValue = 0;
    int sum = 0;

    do {
        sum += fibValue;
        fibIndex += 3; // every third fibonacci is even, if you start at the 2nd term
        fibValue = fibonacci(fibIndex);
    } while (fibValue <= maximum);

    return sum+1; // ???
}

void
euler::problem_0002::solver () {
    std::cout
        << "Problem 0002 Solution: "
        << sumEvenFibonacci(4'000'000)
        << std::endl;
}
