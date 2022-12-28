Name = input("Enter your name :\n")
cap_name = Name[0:].upper()
print("\n\n HELLO", cap_name ,"WELCOME TO ONLINE VOTING \n")
age = int(input(" \n enter your age : \n"))

if (age > 18):
    print("\n You are eligible to vote \n\n\n")
else:
    print("You are not eligible to vote.......!!!! ")