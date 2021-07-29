def vatCalculate(totalPrice=float(input("Enter to product price : "))):
    result = str(totalPrice+(totalPrice*7/100))
    return result + " THB"
print(vatCalculate())