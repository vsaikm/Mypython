import re

pattern = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")

password = 'Sai@123'

result = pattern.fullmatch(password)
print(result.end)

