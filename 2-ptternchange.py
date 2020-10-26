#pipy is a n important website for differnt modules
import re

pattern = re.compile('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

email = 'sai281996@gmail.com'


validation = pattern.search(email)

print(validation.string)

#8 characters long
#contain any sort of letters ,numbers $%#@
