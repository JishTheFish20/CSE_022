loanAmount = int(input("Enter loan amount: "))
loanPeriod = int(input("Enter loan period (months): "))
interestRate = float(input("Enter annual interest rate (percentage): "))

interestRate = (interestRate / 100) / 12

monthlyFee = ((loanAmount * interestRate) * ((1 + interestRate) ** loanPeriod)) / (((1 + interestRate) ** loanPeriod) - 1)


topHalf = ((loanAmount * interestRate) * ((1 + interestRate) ** loanPeriod))
bottomHalf = (((1 + interestRate) ** loanPeriod) - 1)
allTogether = topHalf / bottomHalf

print("You owe $%.2f per month." %monthlyFee)