#This code is to convert celsius to farenheit
celsius = float(input('Enter a value'))
farenheit = (celsius * 1.8 )+ 32
print("%0.1f degree celsius is equal to %0.1f degree farenheit"%(celsius,farenheit))
temp = farenheit
if temp >= 104:
    print ("It's hot")
elif temp <= 50:
    print ("It's cold")
else:
    print("It's nice")