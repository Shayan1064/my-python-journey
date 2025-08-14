s={1,2,4,5,3,7,9,4}
print(s)             # jsut creating set and print it

# methods

# Empty set
empty=set()

#remove
s.remove(9)
print(s)

# add 
s.add(10)
print(s)

# Union 
s1={1,3,5,7,9}
s2={0,2,4,6,8}

# Intersection
print(s1.union(s2))
print(s1.intersection(s2))
