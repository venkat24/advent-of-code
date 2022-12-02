def check(t):
    digits = [int(digit) for digit in str(t)]
    
    assert(len(digits) == 6)

    prev_digit = digits[0]

    double = False
    monotonic = True

    running_count = 1
    running = False

    for i in range(1, 6):
        digit = digits[i]

        if digit < prev_digit:
            monotonic = False
            break

        elif digit == prev_digit:
            running = True
            running_count += 1

        elif digit > prev_digit:
            running = False
            if running_count == 2:
                double = True
            
            running_count = 1

        prev_digit = digit

    if running:
        if running_count == 2:
            double = True

    return double and monotonic

if __name__ == "__main__":
    count = 0

    for t in range(165432, 707913):
        if check(t):
            print(str(t) + " YES")
            count += 1

    print(count)

"""
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""
