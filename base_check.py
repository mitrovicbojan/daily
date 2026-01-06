'''
Base Check
Given a string representing a number, and an integer base from 2 to 36,
determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z
'''

def is_valid_number(n, base):
    base_list = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    if not isinstance(n, str):
        raise TypeError(f"Expected n to be str, got {type(n).__name__}")

    if not isinstance(base, int):
        raise TypeError(f"Expected base to be int, got {type(base).__name__}")

    if not 2 <= base <= 36:
        raise ValueError(f"base must be between 2 and 36, got {base}")
    
    upper_str = n.upper()
    
    is_valid = True   
 
    for char in upper_str:
        if char not in base_list[:base]:
            is_valid = False
            break           
    
    return is_valid

print(is_valid_number("10101", 36))
