#Draw Graph of System of Second ODW
# X' = AX 최대 3차만 ( 4차부터는 그래프를 그리기가 힘들다. )
# 1. 변수의 개수(n)를 입력한다 (1, 2, 3)
# 2. 행렬 A를 입력한다. - square matrix
# 3. 행렬 A의 eigenvalue를 구한다.
# 4. eigenvalue에 따른 eigenvector을 구한다.
# 5. 일반적인 경우에 (n = 2이고 eigenvalue2개)
# 6. X(t) = c1 * Z * e^r1t + c2 * W * e^r2t 모든 t에대해
# 모든t에 대해 그래프를 그리는데 c1, c2는 고정
# 7. x1(t) = c1 * Z1 * e^r1t + c2 * W1 * e^r2t
# 7. x2(t) = c1 * Z2 * e^r1t + c2 * W2 * e^r2t
# 좌표축은 x1, x2 t마다 점을 찍으면 됨

import matplotlib.pyplot as plt
import numpy as np
import math

# 1. 변수의 개수(n)를 입력한다 (1, 2, 3)
#num_of_variables = int(input("변수의 개수를 입력하세요 : ")) # 숫자만 입력하는 것 알아보기
# 2. 행렬 A를 입력한다. - square matrix
matrix_X = np.array([[-3, math.sqrt(2)], [math.sqrt(2), -2]])
# 3. 행렬 A의 eigenvalue를 구한다. 복소수가 나올 수 있기 때문에 직접 계산
def Get_EigenValue():
    eigenvalue1 = -1
    eigenvalue2 = -4
    return eigenvalue1, eigenvalue2

#2차, 3차 근의 공식
def Second_Degree_Root_Formula():
    root = 0
    return root
def Third_Degree_Root_Formula():
    root = 0
    return root

r1, r2 = Get_EigenValue()

#eigenvector은 내가 구하자 계산하기 편한 값이 안나온다.
w, v = np.linalg.eig(matrix_X)
print(w)

c1 = 10
c2 = -10
t = 1.0     #시작을 int로 실수로 해서 계산이 아래 계산이 안됐다.

# 모든t에 대해 그래프를 그리는데 c1, c2는 고정
# 7. x1(t) = c1 * Z1 * e^r1t + c2 * W1 * e^r2t
# 7. x2(t) = c1 * Z2 * e^r1t + c2 * W2 * e^r2t

for t in np.arange(-100, 100, 0.1):
    general_soln1 = c1 * 1 * math.exp(t * w[1]) + c2 * -(2**(1/2)) * math.exp(t * w[0])
    general_soln2 = c1 * 2**(1/2) * math.exp(t * w[1]) + c2 * 1 * math.exp(t * w[0])
    print(t)

    plt.scatter(general_soln1, general_soln2)

#그리드 활성화
plt.grid(True, linestyle = '--')
#축 범위
plt.xlim([-10**2, 10**2])
plt.ylim([-10**2, 10**2])


plt.show()
print(math.exp(2))


