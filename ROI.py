class ROI():
    def __init__ (self, currentROI=0, cashflow=0, expenses={}, income=0):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.currentROI = currentROI

    def calcIncome(self):
        while True:    
            houseinc = input("How much do you plan to charge your tenants per month? Please enter numbers only ")
            if houseinc.isnumeric():
                otherq = input("Does this property have any other source of income? Y/N ")
                if otherq.lower() == 'y':
                    otherinc = input("Please enter the total estimated monthly earnings from all sources")
                    if houseinc.isnumeric():
                        self.income = int(houseinc) + int(otherinc)
                        print(f"Your monthly income is ${self.income}")
                        return self.income
                    else:
                        print("Please enter a number without symbols, punctuation, or letters")
                else:
                    self.income = houseinc
                    print(f"Your monthly income is ${self.income}")   
                    return self.income
            else:
                print("Please enter a number without symbols, punctuation, or letters")




    def calcExpenses(self):
        while True:    
            print("Hello, I am your expense calculator! Please type a category for your expenses. If you want to see your expenses, type 'SEE'. If you want to modify a category, simply type in that category. When you are done, type 'DONE'.")
            houseexp = input("Enter your projected monthly expenses here!")
            if houseexp.lower() == 'done':
                rusure = input("Are you sure? Y/N ")
                if rusure.lower() == 'y':
                    print(f"Your expenses are as summarized: {self.expenses}. Your total expenses are ${sum(self.expenses.values())}")
                    break
            elif houseexp.lower() == 'see':
                print(f"Your projected expenses are as summarized: {self.expenses}. Your total expenses would be ${sum(self.expenses.values())}")          
            else:
                print(f"You have entered '{houseexp}' as an expense. If this was in error, simply type 'BACK'")
                exquant = input("Please enter the amount of the expense (numbers only) ")
                if exquant.isnumeric():
                    self.expenses[houseexp] = int(exquant)
                    print(f"Expense added! Your new projected total is ${sum(self.expenses.values())}")
                elif exquant.lower() == 'back':
                    print("That's alright!")
                else:
                    print("OOPS! You'll need to try that again.")

    def calcCF(self):
        self.cashflow = int(self.income) - sum(self.expenses.values())
        print(f"Your estimated cash flow for this property is ${self.cashflow} per month.")

    def calcROI(self):
        while True:    
            print("Whether you plan to pay for the property in full or make a down-payment for a mortgage, enter that amount here ")
            housecash = input("Please enter numbers only, or type 'BACK' to return to main menu ")
            if housecash.isnumeric():
                print("Please add any other anticipated initial expenses and record the TOTAL here")
                othercash = input("Please enter numbers only, 0 if None ")
                if othercash.isnumeric():
                    initinvest = int(housecash) + int(othercash)
                    self.currentROI = ((self.cashflow * 12) / initinvest) * 100
                    print(f"Your projected ROI for this property as described is {self.currentROI} %")
                    break
                else:
                    print("Please enter numbers only, no symbols or letters")
            elif housecash.lower() == 'quit':
                print("You are going back to the main menu")
                break
            else:
                print("Please enter numbers only, no symbols or letters")

    def ROIcalculator(self):
        while True:
            print("Let's get your ROI calculated! (You can also use me to update a previous record). We will first ask you about the projected income, then expenses, then I will calculate cashflow and ROI.")
            self.calcIncome()
            self.calcExpenses()
            self.calcCF()
            self.calcROI()
            print("Would you like to run the calculation again? Y/N")
            final = input('')
            if final.lower() == 'n':
                print("Thanks for using our calculator!")
                break
            

        




                
            






    

    # def calcCashflow(self):






    # def calcROI(self):

house1 = ROI()
house1.ROIcalculator()