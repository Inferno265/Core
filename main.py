import re
import sys

# Example string
try:
    with open(sys.argv[1], 'r') as file:
        contents = file.read()
except (FileNotFoundError, IndexError) as e:
    print(f'{e}')
    sys.exit(1)

# Regular expressions
msg_pattern = r'\.msg\((.*?)\)'
msg_exclamation_pattern = r'\.msg!\((.*?)\)'  # Pattern for .msg! handling
var_pattern = r'\.var\(.name\("([^"]+)"\)\.value\(([^)]+)\)\)'
vars = {"x": "10"}

# Find all matches
msg_matches = re.findall(msg_pattern, contents)
msg_exclamation_matches = re.findall(msg_exclamation_pattern, contents)
var_matches = re.findall(var_pattern, contents)

# Process .var() pattern
for name, value in var_matches:
    vars[name] = value

# Process .msg() pattern
for msg in msg_matches:
    if msg in vars:
        print(vars[msg])
    else:
        print(f'\033[1;31mCSYNTAX.VAR (1)\033[0m This variable does not exist or is incorrectly allocated within memory. {msg}')

# Process .msg!() pattern for string literals
for msg_exclamation in msg_exclamation_matches:
    # Remove double quotes from the message
    cleaned_msg_exclamation = msg_exclamation.replace('"', '')
    print(cleaned_msg_exclamation)
