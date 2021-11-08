a = int(input("별로 구성된 산의 높이를 정수로 입력하세요:"))
for i in range(a):
    for j in range(2*a):
        if j < a-i-1:
            print(' ', end='')
        elif j <= a+i-1:
            print("*", end='')
        else:
            print(' ', end='')
    print("\n")
        
