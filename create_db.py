import jwt 

print(jwt.decode('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiTWlqYW4iLCJhZ2UiOjIwfQ.T5z17pOk7Sc7zTGelkJeSikPFvnhCO45WWjFIHVphSw' , "some secret" , algorithms=['HS256']))