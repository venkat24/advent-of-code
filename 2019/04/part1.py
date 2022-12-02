from functools import reduce

if __name__ == "__main__":
    count = 0

    for t in range(165432, 707913):
        digits = [int(digit) for digit in str(t)]
        
        assert(len(digits) == 6)

        prev_digit = digits[0]

        double = False
        monotonic = True

        for i in range(1, 6):
            digit = digits[i]
            if digit == prev_digit:
                double = True

            if digit < prev_digit:
                monotonic = False         
                break

            prev_digit = digit
        
        if not monotonic or not double:
            continue

        
        print(str(t) + " YES")
        count += 1

    print(count)

"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 165432-707912.
"""
