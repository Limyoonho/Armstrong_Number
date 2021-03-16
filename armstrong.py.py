'''armstrong number : 153=1^3+5^3+3^3
                    1+125+27=153
                    its a armstrong number'''

#code
a=int(input("Enter the number that you want to check if its armstrong number or not::")) #input for the number
t=a 
s=0
n=len(str(a)) #for the length of the number
while t>0:
    k=t%10 #for separation of the number 
    s+=k**n # "**" is used for power 
    t//=10
if s==a: #if the sum of the power value is equal to the given number 
    print("ARMSTRONG NUMBER!!!!")
else:
    print("Not a armstrong number !!!")
