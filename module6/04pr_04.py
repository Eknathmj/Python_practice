username = input("Enter the username: \n")

# if len(username) < 10:
#     print("Invalid Username  please try aganin")
# else:
#     print("valide username")
 
#  by def methond 

def is_short_username(username):
    if len(username)<10:
        return True
    else:
        return False
    
print(is_short_username (username))
print(is_short_username (username))

