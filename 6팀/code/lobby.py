#curses, tkinter import
from curses.panel import bottom_panel
from tkinter import* 

#버튼 클릭 시 각 게임이 시작 되도록 함수 선언
def open_snake():
    from run_snake import runGame

def open_bomb():
    from run_bomb import runGame

#창 생성
root = Tk()

#창 설정
root.title("게임을 시작하지...")
root.geometry("500x250+700+400")
root.resizable(False, False)

#레이블 생성
pic = PhotoImage(file="./lobbypics/arcade.png")
plabel = Label(root, image=pic)
label = Label(root, text="WELCOME TO PYTHON GAME")

#레이블 배치
plabel.pack(pady=10)
label.pack()

#버튼 생성
pic1 = PhotoImage(file="./lobbypics/snake.png")      #각 버튼의 이미지 지정
pic2 = PhotoImage(file="./lobbypics/bombpic.png")

button1 = Button(root, image=pic1, command=open_snake)
button2 = Button(root, image=pic2, command=open_bomb)
button3 = Button(root, text="quit", width=10, height=1, command=quit)   #나가기 버튼 설정

#버튼 배치
button1.pack(side="left", padx=40) 
button2.pack(side="right", padx=60)
button3.pack(side="bottom", pady=10)

root.mainloop()