#Temperature convertor: F to C
def f_to_c():
    farenheight = input("Please enter the temperature in Farenheight: ")
    celsius = (int(farenheight)-32) * (5/9)
    print(celsius)

#Temperature convertor C to F
def c_to_f():
    celsius = input("Please enter the temperature in Celsius: ")
    farenheight = ((int(celsius)*(9/5)) + 32)
    print(farenheight)

#Gives user input to choose temp they want to convert to
while True:
    type_of_conversion = input("What temperature are you want to convert to? (C/F): ").upper()
    if type_of_conversion == "F":
        f_to_c()
        break
    elif type_of_conversion == "C":
        c_to_f()
        break
    else:
        print("Please enter a C or F")


