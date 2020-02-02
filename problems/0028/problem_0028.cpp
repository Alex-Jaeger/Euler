
#include "problem_0028.hpp"

#include <cmath>
#include <cassert>
#include <iostream>

std::vector<int>
euler::problem_0028::getCornerValues (
    int sidelength
) {
    assert(sidelength % 2 != 0);

    int tr = powf(sidelength, 2);
    int tl = tr - 1*(sidelength-1);
    int bl = tr - 2*(sidelength-1);
    int br = tr - 3*(sidelength-1);

    return {
        tr, tl, bl, br
    };
}

int
euler::problem_0028::sumCornerValues (
    int maxsidelength
) {
    int sum = 1;

    for (int i = 3; i <= maxsidelength; i += 2) {
        std::vector<int> cornerValues = getCornerValues(i);

        for (auto& value : cornerValues) {
            sum += value;
        }
    }

    return sum;
}

void
euler::problem_0028::solver () {
    std::cout
        << "Problem 0028 Solution: "
        << sumCornerValues(1001)
        << std::endl;
}
