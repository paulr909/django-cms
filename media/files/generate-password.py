import string
from random import *

characters = string.ascii_letters + string.digits
password = "".join(choice(characters) for x in range(32))
print(password)
