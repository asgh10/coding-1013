'''
def is_even ( num ):
    if (num % 2) == 0:
        return True
    else:
        return False

if is_even(67) == True:
    print("숫자가 짝수 입니다")
else:
    print("숫자가 홀수 입니다")




def calc_sum_diff(a, b = 10):
    return a + b, a - b

result1 = calc_sum_diff(2, 5)
result2 = calc_sum_diff(2)
print(result1)
print(result2)


def add_ten(num):
    return num + 10

result = add_ten(10)
print(result)
'''

def classify_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


print("------ 홀짝 판별기 ------ (그만 입력 시 종료)")
while True:
    number_str = input("판별할 숫자를 입력해주세요: ")

    if number_str == "그만":
        break
    try:
        number = int(number_str)

        if classify_number(number) == True:
            print(f"{number}은(는) 짝수 입니다")
        else:
            print(f"{number}은(는) 홀수 입니다")  
            
    except ValueError:
        print("숫자를 입력해주세요")    

      

