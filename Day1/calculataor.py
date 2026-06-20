
num1=int(input("enter number 1 :"))
num2=int(input("enter number 2 :"))
print("1.add ,2.sub,3.mul,4.div,5.power,6.modulus")

ch=int(input("enter choice"))

if ch==1:
    print(int(num1+num2))
elif(ch==2):
    print(int(num1-num2))
elif(ch==3):
    print(int(num1*num2))
elif(ch==4):
    print(int(num1/num2))
elif(ch==5):
    print(int(num1**num2))
elif(ch==6):
    print(int(num1%num2))
else:
    print("invalid choice:")
