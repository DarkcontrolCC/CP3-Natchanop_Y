from tkinter import *
import math
def ActiveBMIfunc(event):
    CalBMI=0
    WordBMI=0
    CalBMI=round(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2),1)
    labelResult.configure(text=CalBMI)
    if CalBMI<18.5:
        BMIResult.configure(text="ผอมเกินไป (น้อยกว่า 18.5)",fg="#3399ff")
    elif CalBMI>=18.5 and CalBMI<=22.9:
        BMIResult.configure(text="น้ำหนักปกติ เหมาะสม (18.6 - 22.9)",fg="#00cc00")
    elif CalBMI>=23.0 and CalBMI<=24.9:
        BMIResult.configure(text="น้ำหนักเกิน (23.0 - 24.9)",fg="#cccc00")
    elif CalBMI>=25.0 and CalBMI<=29.9:
        BMIResult.configure(text="อ้วน (25.0 - 29.9)",fg="#ff6600")
    else:
        BMIResult.configure(text="อ้วนมาก (30.0 ขึ้นไป)",fg="#cc0000")
MainWindow = Tk()
MainWindow.geometry("500x300")
labelhead = Label(MainWindow,text="โปรแกรมคำนวนหาค่า BMI",font=("Angsana New",30,"bold"),anchor="center").grid(row=0,column=1)
labelHight=Label(MainWindow,text="ส่วนสูง (m.)",font=("Angsana New",25))
labelHight.grid(row=1,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=1,column=1)
labelWeight=Label(MainWindow,text="น้ำหนัก (Kg.)",font=("Angsana New",25))
labelWeight.grid(row=2,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=2,column=1)
CalcalateButton = Button(MainWindow,text="คำนวณ!",font=("Angsana New",25))
CalcalateButton.grid(row=3,column=0)
CalcalateButton.bind('<Button-1>',ActiveBMIfunc)
labelResult=Label(MainWindow,text="ผลลัพธ์",font=("Angsana New",30,"bold"))
labelResult.grid(row=3,column=1)
BMIResult=Label(MainWindow,text="แปรผล",font=("Angsana New",25))
BMIResult.grid(row=4,column=1)
MainWindow.mainloop()