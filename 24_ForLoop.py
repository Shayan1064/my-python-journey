# Marks=[45,46,43,23,48,49,50,21]
# for marks in Marks:
#     print("Marks :",marks)


#Searching Number
Number=[45,46,43,23,48,49,50,21]
search=50
idx=0
for num in Number:
    if(num==search):
        print("Found at Index : ",idx)
        break
    idx+=1
