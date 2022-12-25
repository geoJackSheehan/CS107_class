// File       : factorial.cpp
// Created    : Fri Nov 19 2021 03:33:24 PM (-0500)
// Author     : Fabian Wermelinger
// Description: Simple recursive function calls (factorial)
// Copyright 2021 Harvard University. All Rights Reserved.

int factorial(int x) // factorial
{
    if (x > 1) {
        return x * factorial(x - 1); // recursive call
    }
    return 1;
}
