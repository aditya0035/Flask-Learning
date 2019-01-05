from Model import db,Puppy,Owner,Toys
rufus=Puppy('Rufus',10)
kim=Puppy('Kim',11)
frank=Puppy("Frank",8)
db.session.add(rufus)
db.session.commit()
db.session.add_all([kim,frank])
db.session.commit()

listOfPuppies=Puppy.query.all()
print(listOfPuppies)

ball=Toys("ball",rufus.id)
ring=Toys("ring",rufus.id)
db.session.add_all([ball,ring])
jose=Owner("Jose",rufus.id)

kimpuppy=Puppy.query.filter_by(name='Kim')
print(f'Kim:{kimpuppy.all()}')

frankpuppy=Puppy.query.get(3)
print(frankpuppy)

print(rufus.Report_Toys())
