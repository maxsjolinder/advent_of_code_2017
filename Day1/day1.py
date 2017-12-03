#!/usr/bin/env python

import sys

def calculate_captcha(input_array, next_step_offset):
    sum = 0
    for i, curr_val in enumerate(input_array):
        consider_next_index = (i + next_step_offset ) % len(input_array) 
        if curr_val == input_array[consider_next_index]:
            sum += curr_val

    return sum

def assert_equal(expected_val, actual_val):
    assert expected_val == actual_val, 'Expected: '+ str(expected_val) + '. Actual: ' + str(actual_val)

def run_tests():
    # Test part 1
    assert_equal(3, calculate_captcha([1,1,2,2], 1))
    assert_equal(4, calculate_captcha([1,1,2,2,1], 1))
    assert_equal(4, calculate_captcha([1,1,1,1], 1))
    assert_equal(0, calculate_captcha([1,2,3,4], 1))
    assert_equal(9, calculate_captcha([9,1,2,1,2,1,2,9], 1))
    
    # Test part 2
    assert_equal(6, calculate_captcha([1,2,1,2], 2))
    assert_equal(0, calculate_captcha([1,2,2,1], 2))
    assert_equal(4, calculate_captcha([1,2,3,4,2,5], 3))
    assert_equal(12, calculate_captcha([1,2,3,1,2,3], 3))
    assert_equal(4, calculate_captcha([1,2,1,3,1,4,1,5], 4))

    print "Tests complete"

def main():
    if len(sys.argv ) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        file = open("input.txt","r")
        raw_input = file.read()
        file.close()
        input_arr = map(int, list(raw_input))
        result_part1 = calculate_captcha(input_arr, 1)
        result_part2 = calculate_captcha(input_arr, len(input_arr)/2)        
        
        print "Day 1, Part 1 Result: ", result_part1
        print "Day 1, Part 2 Result: ", result_part2 

if __name__ == '__main__':
    main()
