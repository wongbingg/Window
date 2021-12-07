import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Wong GUI")
root.geometry("640x480+400+100") #가로x세로

def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")
def warn():
    msgbox.showwarning("경고","해당 좌석은 매진 되었습니다.")
def error():
    msgbox.showerror("오류","오류가 났습니다")
def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아 동반석 입니다. 예매 하시겠습니다?")
def retrycancel():
    msgbox.askretrycancel("확인 / 취소","해당 좌석은 유아 동반석 입니다. 예매 하시겠습니다?")
def yesno():
    msgbox.askyesno("예 아니오","해당 좌석은 역방향입낟?")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None,message="?")
    print("응답:", response)
    if response ==1:
        print('예')
    elif response == 0:
        print("아니오")
    else:
        print("취소")
Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="오류").pack()

Button(root,command=okcancel,text="확인 취소").pack()
Button(root,command=retrycancel,text="재시도 취소").pack()
Button(root,command=yesno,text="재시도 취소").pack()
Button(root,command=yesnocancel,text="재시도 취소").pack()
root.mainloop()