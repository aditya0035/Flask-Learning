from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash,check_password_hash
pwd="MyPassword"
b=Bcrypt()
hashedPassword=b.generate_password_hash(pwd)
print(hashedPassword)
print(b.check_password_hash(hashedPassword,"MyPassword"))
print(generate_password_hash(pwd))
print(check_password_hash(generate_password_hash(pwd),"MyPassword"))
