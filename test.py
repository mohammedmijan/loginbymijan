import bcrypt
 

password = b"password"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.hashpw(password , hashed) == hashed :
    print("Okay")