hourlyWage = int(input('input your hourly wage: '))
regHoursWorked = int(input('input the regular hours worked: '))
overtimeHours = int(input('input your overtime hours: '))
print('your total pay is ', (hourlyWage * regHoursWorked) + ((hourlyWage * 1.5) * overtimeHours))
