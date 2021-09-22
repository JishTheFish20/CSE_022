loanAmount = int(input("Enter loan amount: "))
loanPeriod = int(input("Enter loan period (months): "))

monthlyFee = loanAmount / loanPeriod

print("You owe $%.2f per month." %monthlyFee)
