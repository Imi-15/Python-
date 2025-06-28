print("Loan Calculator")
principal = 1000
years = 0
total = 1000
for years in range (10):
 interest= (principal * 0.05 ) * years
 total += interest
 print("Year", years+1,"is",total,)
