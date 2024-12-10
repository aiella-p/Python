from operator import itemgetter
names = [('Ben','Jones'),('Peter','Parker'),
('Kelly','Isa')]
#Sort names by first name
sorted_names = sorted(names,key=itemgetter(0))
print('Sorted by first name',sorted_names)
# sort names by last name
sorted_names = sorted(names,key=itemgetter(1))
print('Sorted by last name',sorted_names)
# sort names by first name, then last name
sorted_names = sorted(names,key=itemgetter(0,1))
print('Sorted by last name & first name',sorted_names)