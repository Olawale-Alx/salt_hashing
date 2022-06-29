import bcrypt

password = b'falippu'

salt = bcrypt.gensalt(10)
hashed = bcrypt.hashpw(password, salt)

if bcrypt.checkpw(password, hashed) == True:
    print(password)

else:
    print('Wrong hash provided. Authentication failed')
