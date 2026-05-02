# Write a function is_even_two_digit_number that checks whether a given number is an even two digit number.

def is_even_two_digit_number(even):
    return even%2==0 and 10<=abs(even)<100
    
is_even_two_digit_number (24)

is_even_two_digit_number(-19)

