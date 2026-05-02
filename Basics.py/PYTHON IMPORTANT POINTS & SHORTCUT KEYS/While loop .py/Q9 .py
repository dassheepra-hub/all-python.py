####Q9) Write a program to check if a given number.such as 16. is a perfect square

i = 1
square = int(input("enter your no. here = "))
is_perfect_square = False

while i * i <= square:
    if i*i == square:
        is_perfect_square = True
        break
    i += 1
if is_perfect_square :
    print(f'{square}is a perfect square')
else:
    print(f'{square}is not a perfect square')


