# import math
# result = math.gcd(255, 300)
# print(result)

from tkinter import * # *는 모든것을 가져온다(import tkinter와 같음)
window = Tk()
# button = Button(window, text="클릭하세요")
# button.pack() # 압축 배치

# w = Label(window, text="박스 #1", bg= "red", fg= "white")
# w.place(x = 0, y = 0) #place : 절대 배치

# w = Label(window, text="박스 #2", bg= "green", fg= "black")
# w.place(x = 20, y = 20)

# w = Label(window, text="박스 #3", bg= "blue", fg= "white")
# w.place(x = 40, y = 40)

# l1 = Label(window, text="화씨")
# l2 = Label(window, text="섭씨")

# l1.grid(row = 0, column= 0)
# l2.grid(row = 1, column= 0)

# b1 = Button(window, text="화씨 > 섭씨")
# b2 = Button(window, text="섭씨->화씨")
# b1.grid(row = 2, column= 0)
# b2.grid(row = 2, column= 1)

def process():
    print("안녕하세요")

button = Button(window, text="클릭하세요", command= process)
button.pack()

window.mainloop()