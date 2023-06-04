import re
import string

senha = input()

seq = f"{string.ascii_lowercase} {string.ascii_uppercase} {string.digits}"

if not re.match(r"^[a-zA-Z0-9]{6,15}$", senha) or \
    not any(i.islower() for i in senha) or \
    not any(i.isupper() for i in senha) or \
    not any(i.isnumeric() for i in senha) or \
    any(senha[i:i+2] in seq for i in range(len(senha)-2)):
    print("False.")
else:
    print("True.")
