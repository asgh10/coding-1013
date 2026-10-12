def get_average(total_sum = 0, count = 0):
    if count == 0:
        return "입력된 점수가 없습니다."
    
    avg = total_sum / count
    return avg


add = 250
count = 3

result_avg = get_average(add, count)
print(f"평균 점수는 {result_avg}점입니다.")

# 함수를 배울때 꼭 알아두어야 할 포인트
# 변수의 유효 범위 (Scope): 함수 안에서 만든 변수(avg 등)는 함수 밖에서는 사용할 수 없다 이걸 지역 변수라고 표현한다
# 기본값 매개변수 (Default Argument): 매개변수에 미리 기본값을 지정해 둘 수도 있습니다. (def say_hello(name="친구"):)