'''
Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.
'''

def is_balanced(s):
    vowels = ['a','e','i','o','u']
    new_s = list(s.lower())
   
    fisrt_half_count = 0
    second_half_count = 0
    half_s = int(len(new_s) / 2)
    first = new_s[:half_s]
    second = new_s[-half_s:]
  
    for i in first:
        if i in vowels:
            fisrt_half_count +=1
    
    for i in second:
        if i in vowels:
            second_half_count +=1
     
    return fisrt_half_count == second_half_count

print(is_balanced("Kitty Ipsum"))
