

def addSpace(str, newLen):
  
  while (len(str)<newLen):
    str+=" "
    
  return str


downPaymentPercent = 10.00
annualInterestPercent = 12.00
monthlyPaymentPercent = 5.00
listedPurchasePrice = 0.00
listedPurchasePrice = float(input("input the listed price of the item: "))
downPayment = listedPurchasePrice * (downPaymentPercent / 100)
owed = listedPurchasePrice - downPayment+0.00
owedAfterDown = owed
monthlyPayment = owedAfterDown * (monthlyPaymentPercent / 100)

print('your down payment is', downPayment, '$ your monthly payment is', monthlyPayment,
      "$ the anual interest rate is 12%")
      
monthNumber = 1
print(addSpace("month",14)+ addSpace("balance",14)+ addSpace("intrest",14)+addSpace("principal",10)+addSpace("ending banance",14))
while owed > 0:

    interest = owed * (1 / 100)
    owed = (owed + interest)
    if monthlyPayment > owed:
        monthlyPayment = owed
    owed = round(owed, 2)
    interest = round(interest, 2)
    monthlyPayment = round(monthlyPayment, 2)
    print(addSpace(str(monthNumber),14), addSpace(str(owed),14), addSpace(str(interest),14),addSpace(str(monthlyPayment),14),addSpace(str(round(owed-monthlyPayment,2)),14))
    owed -= monthlyPayment
    monthNumber += 1
    if monthNumber > 50:
        break
        
