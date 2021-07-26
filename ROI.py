    """
        About the class:
        I designed this calculator to be one shot per execution, with a small twist in expenses.
        The class takes the calculated ROI, the calculated cashflow, the income, and a dictionary 
        containing all of the recorded expenses.
    """

class ROI():
    def __init__ (self, currentROI=0, cashflow=0, expenses={}, income=0):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.currentROI = currentROI
    
    """
        calcIncome takes rent as an initial input(must be numbers ONLY, no punctuation),
        then asks the user to provide the TOTAL monthly income projected to be gained from
        other sources. I was led to believe that this is not usually a large sum so I did not 
        make a list or dictionary for storing potential sources of extra income.
    """

    def calcIncome(self):
        while True:    
            houseinc = input("How much do you plan to charge your tenants per month? Please enter numbers only ")
            if houseinc.isnumeric():
                otherq = input("Does this property have any other source of income? Y/N ")
                if otherq.lower() == 'y':
                    otherinc = input("Please enter the total estimated monthly earnings from all sources ")
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

    """
        The function calcExpenses asks the user to input a name or category for a monthly expense, and then asks for the respective amount 
        of money. It will repeat this process until the user indicates they are "done". The user can view expenses
        by typing "see". This command will print the dictionary and provide a calculated total. The total should update
        as expenses are added, modified, and removed.
    """


    def calcExpenses(self):
        while True:    
            print("Hello, I am your expense calculator! Please type a CATEGORY or name for your monthly expense. If you want to see your expenses, type 'SEE'. If you want to modify a category, simply type in that category. When you are done, type 'DONE'.")
            houseexp = input("Enter your projected monthly expenses here! ")
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

    """
        calcCF is pretty self-explanatory. It subtracts monthly expenses from monthly income to produce 
        the monthly cashflow.
    """                

    def calcCF(self):
        self.cashflow = int(self.income) - sum(self.expenses.values())
        print(f"Your estimated cash flow for this property is ${self.cashflow} per month.")

    """
        calcROI first asks the user to enter all projected initial expenditures. This is done in a fassion very similar 
        to how calcIncome works. the option 'BACK' is included in the chance that user would like to update expenses or 
        income again before proceeding with the final calculation. The ROI calculation was created in accordance with the 
        Bigger Pockets video. 
    """
    def calcROI(self):
        while True:    
            print("Whether you plan to pay for the property in full or make a down-payment for a mortgage, enter that amount here")
            housecash = input("Please enter numbers only, or type 'BACK' to return to the main menu ")
            if housecash.isnumeric():
                print("Please add any other anticipated initial expenses and record the TOTAL of these other expenses here")
                othercash = input("Please enter numbers only, or 0 if you don't anticipate any extra expenses")
                if othercash.isnumeric():
                    initinvest = int(housecash) + int(othercash)
                    self.currentROI = ((self.cashflow * 12) / initinvest) * 100
                    print(f"Your projected ROI for this property as described is {self.currentROI} %")
                    break
                else:
                    print("Please enter numbers only, no symbols or letters")
            elif housecash.lower() == 'back':
                print("You are going back to the main menu")
                break
            else:
                print("Please enter numbers only, no symbols or letters")

    """
        The calculator forces the user to go through the process in the order shown in the Bigger Pockets video. 
        Once ROI has been calculated, the user has the option to go through the calcuation again, or quit. 
    """

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


house1 = ROI()
house1.ROIcalculator()