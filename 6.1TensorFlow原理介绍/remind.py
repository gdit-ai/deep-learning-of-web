#-*- conding:utf-8 -*-
import datetime
import time #时间函数
import tkinter.messagebox #tk消息框
timelist=['8:55:00','9:50:00','10:55:00',"11:50:00","14:45:00","15:40:00","16:45:00","17:40:00","18:55:00","19:50:00","20:45:00","21:40:00"]    #自定义提醒时间
while True:
    now=time.strftime('%H:%M:%S',time.localtime(time.time()))      #获取为HH:MM:SS时间格式
    for i in timelist:
        if i==now:
            print("到达设定时间:",now)
            win = tkinter.Tk()  # 初始化Tk
            win.title("当前时间")
            win.attributes("-topmost", True)
            win.geometry("%dx%d" % (1000, 1000))
            TimeLabel = tkinter.Label(text="下课了", bg='red', font=('Arial', 150), width=300, height=200)
            TimeLabel.pack()
            win.mainloop()




