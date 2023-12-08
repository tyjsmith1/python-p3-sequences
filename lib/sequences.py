#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    fibonacci = []

    for num in range(length):
        fibonacci.append(a)
        a, b = b, a + b
    print(fibonacci)