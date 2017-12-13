#!/usr/bin/env python

import sys
def calculate_checksum(input_2D_list):
    checksum = 0
    for row in input_2D_list:
        checksum += get_row_checksum(row)
    return checksum

def get_row_checksum(row):
    return max(row) - min(row)

def calculate_divisible_checksum(input_2D_list):
    checksum = 0
    for row in input_2D_list:
        checksum += calculate_divisible_row_checksum(row)
    return checksum
    
def calculate_divisible_row_checksum(row_list):
    checksum = 0
    for i, val1 in enumerate(row_list):
        for j, val2 in enumerate(row_list):
            if i != j:
              
                if is_evenly_divisible(val1, val2):
                    return divide_largest_with_smallest(val1, val2)
    return checksum

def divide_largest_with_smallest(val1, val2):
    if val1 > val2:
        return val1 / val2
    else:
        return val2 / val1 

def is_evenly_divisible(val1, val2):
    mod = -1
    if val1 > val2:
        mod = val1 % val2
    else:
        mod = val2 % val1       
    return mod == 0

def run_tests():
    assert calculate_checksum([[5,1,9,5],[7,5,3],[2,4,6,8]]) == 18
    assert is_evenly_divisible(2, 8) == True
    assert is_evenly_divisible(8, 2) == True
    assert is_evenly_divisible(5, 2) == False
    assert is_evenly_divisible(2, 5) == False
    assert calculate_divisible_row_checksum([5,9,2,8]) == 4
    assert calculate_divisible_row_checksum([9,4,7,3]) == 3
    assert calculate_divisible_row_checksum([3,8,6,5]) == 2
    assert calculate_divisible_checksum([[5,9,2,8],[9,4,7,3],[3,8,6,5]]) == 9
    print "Test run to completion"

def main():
    if should_run_tests():
        run_tests()
    else:
       input_list = get_input_list()
       result_part1 = calculate_checksum(input_list)
       print "Day 2, part 1 Result : " , result_part1
       result_part2 = calculate_divisible_checksum(input_list)
       print "Day 2, part 2 Result : " , result_part2

def get_input_list():
    file = open("input.txt", "r")
    input = file.read()
    file.close()
    string_2d_list = [r.split() for r in input.split("\n")]
    int_2d_list = [map(int, row) for row in string_2d_list]
    return int_2d_list


def should_run_tests():
    return len(sys.argv) > 1 and sys.argv[1] == "test"

if __name__ == '__main__':
    main()


