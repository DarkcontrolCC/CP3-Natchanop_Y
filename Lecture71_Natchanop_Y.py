menuList =[]
priceList = []

def showBill():
    totalPrice=0
    print("---- My food ร้านอาหารของฉัน ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice +=int(priceList[number])
    print('ต้องชำระ :',totalPrice)
while True:
   menuName = input("กรอกชื่อเมนู : ")
   if(menuName.lower()=='ออก'):
       break
   else:
       menuPrice = input('ราคาอาหาร : ')
       menuList.append(menuName)
       priceList.append(menuPrice)
showBill()