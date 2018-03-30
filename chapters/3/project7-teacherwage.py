# salary calculator
startSalary = 0
percentageInc = 0
numberOfYears = 0
startSalary = float(input("input your starting Salary: "))
percentageInc = float(input("input your yearly percent increase: "))
numberOfYears = int(input('input the number of years you plan to work: '))
currentSalary = startSalary
for year in range(1, numberOfYears + 1):
    print('on year', year, 'you should earn', currentSalary)
    currentSalary += currentSalary * (percentageInc / 100)
