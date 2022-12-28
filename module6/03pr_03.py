text = input("enter the text \n")
if ("make a lot of money" in text):
    spam = True
elif ("subcribe my chilnal for free" in text):
    spam = True
elif ("buy now" in text):
    spam = True
else:
    spam = False


if(spam):
    print("This IS the spam")
else:
    print("This is not a spam")

