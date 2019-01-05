from SQLDatabaseWithFalsk17 import dbInstance, Puppy
#create Puppy
my_puppy=Puppy('Rufus',5)
dbInstance.session.add(my_puppy)
dbInstance.session.commit()

#Read a record

all_puppies=Puppy.query.all()
print(f"All Puppies:{all_puppies}")

#select by id Primary key
puppy=Puppy.query.get(1)
print(f"Select by Id:{puppy}")
#filter
puppies=Puppy.query.filter_by(name="Rufus")
print(f'Select By Filter:{puppies.all()}')
#update
rufus=Puppy.query.filter_by(name="Rufus").first()
rufus.age=18
dbInstance.session.add(rufus)
dbInstance.session.commit()

#delet
firstPuppy=Puppy.query.get(1)
dbInstance.session.delete(firstPuppy)
dbInstance.session.commit()

#Read a record

all_puppies=Puppy.query.all()
print(f"All Puppies:{all_puppies}")
