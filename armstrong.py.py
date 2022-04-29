'''armstrong number : 153=1^3+5^3+3^3
                    1+125+27=153
                    its a armstrong number'''

# code
num = int(input("Enter the number that you want to check if it's armstrong number or not : ")) # 판단할 숫자 입력
sum = 0
temp = num                  # num의 값을 while에서 바꾸기 위해 설정

while temp > 0:             # 입력 수의 몫이 0이 될 때까지 반복
    digit = temp % 10       # 입력숫자를 10으로 나눈 나머지 값으로 각 자리 숫자를 찾음
    sum += digit ** 3       # 암스트롱의 수를 구하기 위해 자릿수를 세제곱 후 합산
    temp //= 10             # temp에 몫 값을 설정함

if sum == num:              # 각 자릿수의 세제곱한 값의 총합과 입력값이 일치하는 지 비교
    print(num, "IS ARMSTRONG NUMBER!!!")
else:
    print(num, "is not a armstrong number!!!")