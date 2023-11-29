investment = input("How much did you invest? ")
interestRate = input("How much is the interest rate: ")
investment = float(investment)
interestRate = float(interestRate) / 100
for i in range(10):
    investment = investment + (investment * interestRate)
    print("Total earnings for year {:d} are {:.2f}".format(i, investment))
