#Subsidized Direct Federal Loan Calculator
p = float(input('How much money would you like to borrow?\n'))
y = float(input('How many years would you like the loan for?\n'))
t = 12.0
i = 0.034
f = 0.01051
m = ((p * i)/(t * (1-(1+(i/t))**((-y) * t))))
b = m * t * y
iP = b - p
fee = p * f
print('Subsidized Direct Federal Loan')
print('Principle: $', round(p,2))
print('Interest Rate:', round(i * 100,2), '%')
print('Years:', int(y))
print('Monthly Payment: $', round(m,2))
print('Total Paid on Loan: $', round(b,2))
print('Total Interest Paid: $', round(iP,2))
print('Additional Fees Paid: $', round(fee,2))
print('Total Costs Over Principle: $', round(fee + iP,2))
