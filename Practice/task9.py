'''Take five numbers as input representing marks obtained and total marks.
Display the percentage.'''

sub1=int(input("Enter First Subject Mark : "))
sub2=int(input("Enter Second Subject Mark : "))
sub3=int(input("Enter Third Subject Mark : "))
sub4=int(input("Enter Fourth Subject Mark : "))
sub5=int(input("Enter Fifth Subject Mark : "))

total=sub1+sub2+sub3+sub4+sub5
print("Here is Total : ",total)


per=total/5
print("Here is Percantage : ",per)



