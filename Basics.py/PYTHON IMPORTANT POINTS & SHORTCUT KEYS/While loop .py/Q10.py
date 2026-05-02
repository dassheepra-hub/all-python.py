####Q10) Write a program to count occurrences of the character "s" in the string "success"
word = input("write your word here = ")
char_to_count = input("enter a character to count = ")
index = 0
count = 0
while index < len(word):
    if word[index] == char_to_count:
        count+= 1
    index += 1
print(f"{char_to_count} = {count}")
