# write code if the following words are in meseege then print it this is spam

m1="Click this"
m2="subscribe now"
m3="buy now"
m4="make money online"

messege=input("Enter your comment")

if((m1 in messege) or (m2 in messege) or (m3 in messege) or (m4 in messege)):
    print("This is Spam")
else:
    print("This is not a Spam")