SystemMenu ={'ข้าวหมกไก่':45,'ข้าวมันไก้':40,'ข้าวมันไก่รวมมิตร':55,'ข้าวรวมมิตรพิเศษ':70}
menuList =[]
def showBill():
    print("---- My food ร้านอาหารของฉัน ----".center(50,'-'))
    total_price=0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total_price += (menuList[number][1])
    print("\nจำนวนสินค้าทั้งหมดเป็น", (number+ 1), "รายการ", "รวมเป็นจำนวนเงินทั้งหมด", total_price, "บาท")
while True:
   menuName = input("กรอกชื่อเมนู : ")
   if(menuName.lower()=='exit'or menuName=='ออก'):
       break
   else:
       menuList.append([menuName,SystemMenu[menuName]])
showBill()