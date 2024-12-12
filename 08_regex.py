import re

def check_phone_number(text):
    
    pattern = r'^(\+420)?\s?\d{3}\s?\d{3}\s?\d{3}$'
    
    return bool(re.fullmatch(pattern, text.strip()))

# Test cases
print(check_phone_number('test'))  # -> False
print(check_phone_number('608 192 292'))  # -> True
print(check_phone_number('+420 608 192 292'))  # -> True
print(check_phone_number('+420608192292'))  # -> True
print(check_phone_number('608192292...'))  # -> False
