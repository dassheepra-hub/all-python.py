####Q6) write a program to count the number of consonant in the word "learning"
# input = "learning"
# Output = " 5" 
word = "learning"
vowels = "aeiou"
count = 0
index = 0
while index < len(word):
    if word[index].lower() not in vowels and word[index].isalpha():
        count += 1
    index += 1
print("consonant in word is = ", count)

        
