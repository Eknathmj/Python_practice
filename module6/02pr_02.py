sub1 = int(input("Enter the marks of sub1 : \t"))
sub2 = int(input("Enter the marks of sub2 : \t"))
sub3 = int(input("Enter the marks of sub3 : \t"))
if(sub1<33 or sub2<33 or sub3<33):
    print("Fail due to marks are less than 33 in each subject")
elif((sub3+sub1+sub2)/3 < 40):
    print("you are fail due to less marks in all the three sunjects")
else:
    print("congratulations ! you are passed")