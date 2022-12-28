latter = ('''Hello Dear!! Enter your name :  abc  \n  please note that your name will be saved in 
our data base \t plase enter date : xyz''')
name = input(" Enter name : \n")
date = input(" date : \n")
latter = latter.replace("abc", name)
latter = latter.replace("xyz", date)
print(latter)