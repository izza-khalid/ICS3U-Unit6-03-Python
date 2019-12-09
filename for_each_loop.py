#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: Dec 2019
# This program uses for...each loops

import random


def max_of_numbers(list_of_numbers):
    # this function finds the minimum number in the list

    minimum = list_of_numbers[0]

    for counter in list_of_numbers:
        if minimum > counter:
            minimum = counter

    return minimum


def main():
    # this function uses a list

    random_numbers = []
    sum = 0

    # input
    print("The numbers are ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    sum = max_of_numbers(random_numbers)

    print("The smallest of all these numbers is: {0} ".format(sum))


if __name__ == "__main__":
    main()
