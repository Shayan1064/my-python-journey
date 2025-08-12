# Question NO:1 
                # write code to make file and write some data in it 

with open("Simple.text","w") as sha:
    sha.write("Hello I am Shayan Hassan\nI am CS student\nI am learning Python")

#-------------------------------------------------------------------------------------------

# Question NO:1 
                # write code to replace the python with Machine Learning

with open("Simple.text","r") as yan:
    data=yan.read()
    print(data)

    new_data=data.replace("Python","Machine Learning")
    print(new_data)

#------------------------------------------------------------------------------------------------

# Question NO:1 
                # write code to find the data if found then print YES and if not then print NO
word="Shayan"
with open("Simple.text","r") as Noman:
    data=Noman.read()
    if(word=="Shayan"):
        print("Yes")
    else:
        "NO"

