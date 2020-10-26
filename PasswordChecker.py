#how many times our password has been hacked

#hackers work

#https://haveibeenpwned.com/
#hackers use something called dictionary attacks ...uses a massive dictionary ...tries to login to website
#looping through these and hit

#we need to istall requests module

import requests

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'#<Response [200]>
#hashing is done here without reveasling the identity the original passwords passed into hashing algorithm ..we get the hshed version of the password
#use k anonimity (for privacy) we only give first five characters of hashed one
#api has all the passwords ..api look into the database that  matches the first five characters and get all  the passwords
res = requests.get(url)

print(res)#<Response [400]> -it is not good we must get 200 which is ok

#sha1 ,md5 hash generaror
#we cannot know the password given in the box by using the hash version this is clled idempotent
give an input alwys gives same output 


