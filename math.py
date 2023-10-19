# 두 숫자를 입력
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 덧셈
addition = num1 + num2
print("덧셈 결과:", addition)

# 뺄셈
subtraction = num1 - num2
print("뺄셈 결과:", subtraction)

# 곱셈
multiplication = num1 * num2
print("곱셈 결과:", multiplication)

# 나눗셈
if num2 != 0:
    division = num1 / num2
    print("나눗셈 결과:", division)
else:
    print("0으로 나눌 수 없습니다.")

