a=int(input("Enter the number that you want to check if its armstrong number or not::"))
t=a
s=0
n=len(str(a))
while t>0:
    k=t%10
    s+=k**n
    t//=10
if s==a:
    print("ARMSTRONG NUMBER!!!!")
else:
    print("Not a armstrong number !!!")
