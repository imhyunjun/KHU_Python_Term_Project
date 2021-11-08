
weight = float(input("무게(킬로그램):"))
height = float(input("키(미터):"))

BMI = weight / (height ** 2)

print("당신의 BMI: ", BMI)

if BMI < 25:
    print("정상입니다.")
elif BMI < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")
