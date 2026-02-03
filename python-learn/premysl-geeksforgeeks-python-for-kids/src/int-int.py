#!/usr/bin/env python3
n = int(input("Enter the size of list : "))
lst = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)