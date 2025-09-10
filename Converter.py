print("Hello, please enter a temperature in degrees Fahrenheit")
temp=int(input())
Cel=(temp-32)*5.0/9
Cel=Cel.__round__(0)
print(temp, "degrees Fahrenheit is ", int(Cel), "degrees Celsius")