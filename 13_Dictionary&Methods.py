Class9th={
    "Shayan":100,
    "Noman":99,
    "Sanan":98,
    "Hamdan":97,
    "Ayyan":96
}
print(Class9th)

# Methods

print(Class9th.items()) # give you each key and its vlaue in tuple
print(Class9th.keys())  # gives you only the keys in dic
Class9th.update({"Saadat":95})
print(Class9th)
print(Class9th.values()) 
# and more.........S

for i in Class9th:
    if(i>=97):
        print("you are selected")
    else:
        print("Youa are not")