
#Use with to read data from file

with open("Demo.text","r") as sha:
    data=sha.read()
    print(data)

#use with to write data in file

with open("Demo.text","w") as yan:
    yan.write("I will be the Data Engineer")

# use with to append data in file

with open("Demo.text","a") as noman:
    noman.write("\nand also Python Developer ")