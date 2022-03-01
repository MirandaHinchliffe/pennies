Money = float(input("Enter Change Amount: "))

Dollars = int(Money/100)
Money %= 100
Quarters = int(Money/25)
Money %= 25
Dimes = int(Money/10)
Money %= 10
Nickels = int(Money/5)
Money %= 5
Pennies = int(Money/1)

print('Dollars: ' + str(Dollars)) 
print('Quarters: ' + str(Quarters)) 
('Dimes: ' + str(Dimes)) 
print ('Nickels: ' + str(Nickels)) 
print ('Pennies: ' + str(Pennies)) 