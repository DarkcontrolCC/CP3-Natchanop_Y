Usernameinput=input("Username : ")
Passwordinput=input("Password : ")
if Usernameinput == "Admin" and Passwordinput == "1123":
    print("Welcome !")
    print("Please select Product list")
    print("1.Banana : 20 THB")
    print("2.Apple : 5 THB")
    print("3.watermelon :30 THB")
    CustomerSelc=int(input("Product Number : "))
    if CustomerSelc == 1:
        print("Select Banana 20 THB/Unit")
        BananaAmount=int(input("Amount : "))
        RateBanana=20
        print("Result price = ",BananaAmount*RateBanana,"THB")
    elif CustomerSelc == 2:
        print("Select Apple 5 THB/Unit")
        AppleAmount = int(input("Amount : "))
        RateApple = 5
        print("Result price = ", AppleAmount * RateApple, "THB")
    elif CustomerSelc == 3:
        print("Select Watermelon 30 THB/Unit")
        WaterMelonAmount = int(input("Amount : "))
        RateWaterMelon = 30
        print("Result price = ", WaterMelonAmount * RateWaterMelon, "THB")