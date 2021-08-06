##import libraly
from forex_python.bitcoin import BtcConverter
from tkinter import *
from datetime import *
root = Tk()
root.title("Bitcoin convert")
root.geometry("600x150")

##Defind Function
def Btc_convert(event):
    Btc_Covert="{:,}".format(round(BTC_keep.convert_btc_to_cur((float(textBoxBTC.get())), 'THB'),2))
    Btc_Covert=str(Btc_Covert)+" THB"
    label4.configure(text=Btc_Covert)

#BTC Defind
BTCPrevious1Day = datetime.today() - timedelta(days = 1)
BTC_keep = BtcConverter()
Btc_Getlatest="{:,}".format(round(BTC_keep.get_latest_price('THB'),2))
Btc_GetPrecios1Day="{:,}".format(round((BTC_keep.get_previous_price('THB', BTCPrevious1Day)),2))
Btc_different="{:,}".format(round(BTC_keep.get_latest_price('THB')-BTC_keep.get_previous_price('THB', BTCPrevious1Day),2))

#Word assembly
Word0 = "Bitcoin price yesterday : "
Word1 = str(Btc_GetPrecios1Day)+" THB"
Word2 = "Bitcoin price now : "
Word3 = str(Btc_Getlatest)+" THB"

#Word place
label0 = Label(root,text=Word0,font=("16"))
label0.grid(row=0,column=0)
label1 = Label(root,text=Word1,font=("16"))
label1.grid(row=0,column=1)
label2 = Label(root,text=Word2,font=("16"))
label2.grid(row=1,column=0)
label3 = Label(root,text=Word3,font=("16"))
label3.grid(row=1,column=1)
textBoxBTC = Entry(root,font="50")
textBoxBTC.grid(row=2,column=0)
label4 = Label(root, text="Result", font=("Verdana 15 underline"), anchor=W)
label4.grid(row=2,column=1)
label5 = Label(root, text="("+str(Btc_different)+")", font=("Verdana 15 underline"),fg="gray")
label5.grid(row=1,column=2)
CalcalateButton = Button(root,text="Convert ! ",font=("12"))
CalcalateButton.grid(row=3,column=0)
CalcalateButton.bind('<Button-1>',Btc_convert)

#Show window and run
root.mainloop()