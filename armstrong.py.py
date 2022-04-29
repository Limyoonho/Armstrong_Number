'''armstrong number : 153=1^3+5^3+3^3
                    1+125+27=153
                    its a armstrong number'''

#code
num = int(input("Enter the number that you want to check if its armstrong number or not::")) #input for the number
sum = 0
temp = num

while temp > 0:
    digit = temp % 10 #for separation of the number 
    sum += digit ** 3 # "**" is used for power 
    temp //= 10

if sum == num: #if the sum of the power value is equal to the given number 
    print("ARMSTRONG NUMBER!!!!")
else:
    print("Not a armstrong number !!!")