def login():
    Usernameinput = input("ชื่อผู้ใช้ : ")
    Passwordinput = input("รหัสผ่าน : ")
    if Usernameinput == "Admin" and Passwordinput == "1123":
        print("เข้าใช้งานสำเร็จ")
    else:
        print("ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง")
        login()
def showmenu():
    print("โปรแกรมคำนวณภาษีมูลค่าเพิ่ม")
    print("โปรดเลือกฟังก์ชั้นการทำงาน")
    print("1. คำนวณภาษี")
    print("2. คำนวนราคา")
def menuSelect():
    userSelected=int(input(">> "))
    if userSelected == 1:
        price = int(input("ราคาสินค้า: "))
        print("ราคาสินค้า กับ ภาษีมูลค่าเพิ่ม : ", vatCalculate(price), "THB")
        print("")
    elif userSelected == 2:
        print("ราคาสินค้า กับ ภาษีมูลค่าเพิ่ม : ", priceCalculate(),"THB")
    else:
        print("กรุณาเลือกหมายเลขใหม่ เลือกหมายเลขไม่ถูกต้อง")
        menuSelect()
def vatCalculate(totalPrice):
    vat = 7 / 100
    result = totalPrice + (totalPrice*vat)
    return result
def priceCalculate():
    price1 = int(input("สินค้าชิ้นที่ 1 >> "))
    price2 = int(input("สินค้าชิ้นที่ 2 >> "))
    return vatCalculate(price1+price2)
login()
showmenu()
menuSelect()