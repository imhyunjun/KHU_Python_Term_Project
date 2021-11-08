#초기화
name = "이름"
major = "학과"
dream = "장래희망"
bYear = 1996
bMonth = 4
bDay = 3

currY = 2021
currM = 9
currD = 18

gYear = 3000

#문자열로 입력 받아 int형으로 변환하게 할 임시 변수들
tempY = "Y"
tempM = "M"
tempD = "D"

#입력
name, major, dream, tempY, tempM, tempD = input("이름, 학과, 장래 희망, 출생년도, 생일(월), 생일(일) 을 ','로 구분하여 입력하시오 : ").split(',')

bYear = int(tempY)
bMonth = int(tempM)
bDay = int(tempD)

#만나이 계산( 아무리 생각해도 조건같은게 있어야 할 것 같아서 조건문이란 것을 공부해서 썼습니다. )
if bMonth < currM:
    gYear = 30 + bYear
elif bMonth == currM:
    if(bDay <= currD):
        gYear = 30 + bYear
else:
    gYear = 31 + bYear

print(major,"을(를) 졸업하신 ",name,"님은 ",gYear,"년", currM,"월", currD,"일 당신이 희망하셨던 ",dream,"이(가) 되셨습니다. 축하드립니다")
