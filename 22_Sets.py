Set1={1,2,3,4,5,6}
print("This is your Set 1 collection")
print(Set1)

print()

set2={"Shayan",1223,23,("Shayan","Noman")}
print("This is your set 2 Elements")
print(set2)


#set methods

Laptop=set() #take an empty set in this way

Laptop.add(2)
Laptop.add(3)
Laptop.add(4)
Laptop.add(2)
Laptop.add("Shayan")
Laptop.add(("Noman","Hamdan"))

print("This is your Laptop set : ",Laptop)

Laptop.remove("Shayan")
print(Laptop)

#Union in sets

s1={0,2,4,6,8}
s2={1,3,5,7,9}

print(s1.union(s2))

print(s1.intersection(s2)) #intersection in set
