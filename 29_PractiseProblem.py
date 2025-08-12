
# write function that print your name 
print("Enter your name :")
name=input()

def greet(name):
    print("Hello :",name)

greet(name)

while True:
    print("Enter your word :")
    word=input()
    if(word=="exit"):
        break

    def pilendrome(word):
        if (word==word[::-1]):   #(word==word[::-1]) this will give you reverse of anything
             print("Pilendrome")
        else:
            print("Not Pilendrome")
    pilendrome(word)
