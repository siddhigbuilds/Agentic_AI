
print("ENTER TOTAL MARKS OF STUDNET :")

total=int(input())

if total>=80 and total<=100:
    print("A+")

elif total>=75 and total<80:
    print("A")

elif total>=60 and total<75:
    print("B")

elif total>=35 and total<60:
    print("C")

else:
    print("faild")