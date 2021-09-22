currentBalance = int(input("Enter your current bank balance: "))
monthlyFee = int(input("Projected monthly operational expenses: "))
monthlyIncome = int(input("Projected monthly income from operations: "))

netBurnRate = monthlyFee - monthlyIncome
projectedRunway = currentBalance/netBurnRate


print("Gross burn rate: $%i" %monthlyFee)
print("Net burn rate: $%i" %netBurnRate)
print("Projected runway: %i months" %projectedRunway)