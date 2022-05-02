'''armstrong number : 153=1^3+5^3+3^3
                    1+125+27=153
                    its a armstrong number'''

# code
num = int(input("Enter the number that you want to check if it's armstrong number or not : ")) # 판단할 숫자 입력
sum = 0
temp = num                  # num의 값을 while에서 바꾸기 위해 설정
arms_list = []              # 암스트롱의 수들을 리스트로 저장(5/2 추가)

while temp > 0:             # 입력 수의 몫이 0이 될 때까지 반복
    digit = temp % 10       # 입력숫자를 10으로 나눈 나머지 값으로 각 자리 숫자를 찾음
    sum += digit ** 3       # 암스트롱의 수를 구하기 위해 자릿수를 세제곱 후 합산
    temp //= 10             # temp에 몫 값을 설정함

if sum == num:              # 각 자릿수의 세제곱한 값의 총합과 입력값이 일치하는 지 비교
    print(num, "IS ARMSTRONG NUMBER!!!\n")
else:
    print(num, "is not a armstrong number!!!\n")

# new(5/2 추가)
def get_arms():             # 잘못 입력했을 경우 계속 입력이 가능하도록 함수로 구현
    sum = 0
    temp = 0
    arms = input("Want to know more Armstrong numbers?(Y/N) : ")
    if arms == "Y" or arms == "y":
        for temp in range(1, 1001):         # 1부터 1000까지의 암스트롱의 수를 찾음, 10000까지도 해보았으나 결과가 같아 패스
            j = temp
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            temp = j
            if sum == temp:
                arms_list.append(temp)
            sum = 0
        for element in arms_list:
            print(element, end='\n')
    elif arms == "N" or arms == "n":
        print("End")
    else:
        get_arms()

get_arms()                 # 함수 호출