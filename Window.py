#윈도우 조작, 화면 배치 등

from tkinter import *
import tkinter
mainWindow = Tk()

screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()

#변수 타입 어노테이션을 이용한 힌트
def SetWindowSize(_window : tkinter.Tk, _height : float, _width :float) -> None:
    print(_height, _width)

SetWindowSize(mainWindow, 100.0, 100.0)

mainloop()
