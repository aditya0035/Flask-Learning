from SQLDatabaseWithFalsk17 import Puppy,dbInstance
#this will create all tables
dbInstance.create_all()

sam=Puppy("Sammy",8)
frank=Puppy("Frank",10)

print(sam.id)
print(frank.id)

dbInstance.session.add(sam)
dbInstance.session.add_all([frank])
dbInstance.session.commit()
print(sam.id)
print(frank.id)
