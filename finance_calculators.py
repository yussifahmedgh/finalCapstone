#started by importing math to be used later in a code block
import math

#print user input choices to run the program
#user have to choose one of these choices calculate their return on investment or interest to be paid at a certain time
print("\nInvestment - To calculate the amount of interest you'll earn on your investment")
print("\nBond - To calculate the amount you'll have to pay on a home loan")


#user has to choose either investment or bond to proceed
while True:
      option = input("\nEnter either 'investment' or 'bond' from the choices above to proceed").lower().strip()
      if option == "investment":


       # Under investment option, user have to choose their choice of interest
       # if wrong options is selected program repeats until correct option is entered
       while True:     
            inv_option = input("\nChoose either 'simple' or 'compound' interest").lower().strip()


            #if user chooses simple or compound, user is requested to enter needed information to run formula
            #'try and except' is used to handle wrong input and code repeats until all inputs are correct and in right format
            #interest_amount is devided by 100 to get the correct percentage
            #once all input are valid, formnula runs and output is displayed for user
            
            if inv_option == "simple":
                try:   
                    deposit_amount = float(input("\nPlease enter the deposit amount"))
                    interest_amount = float(input("\nPlease enter interest number only without percentage"))/100
                    year_inv = float(input("\nPlease enter years of investment"))
                    total_simple = deposit_amount * (1 + interest_amount * year_inv) 
                    print(f"\nYour simple interest within the specified time is {total_simple}")
                    break
                except:
                    print("Please enter a numberic character")
                continue

            elif inv_option == "compound":
                try:    
                    deposit_amount = float(input("\nPlease enter the deposit amount"))
                    interest_amount = float(input("\nPlease enter interest amount only"))/100
                    year_inv = float(input("\nPlease enter years of investment"))
                    total_compound = deposit_amount * math.pow((1 + interest_amount), year_inv)
                    print(f"\nYour compound interest within the specified time is {total_compound}")
                    break
                except:
                    print("Error, Please enter a numberic character only")
                continue

            else:
                print("Invalid option, please choose a correct option")
       break
      

      # if user chooses bond, then they are prompted to enter required information to run formale below
      #again try and except is used to handle any kind of error
      elif option == "bond":
            try:
                house_value = float(input("\nPlease enter the present value of the house"))
                interest_rate = float(input("\nPlease enter interest rate"))
                repay_month = float(input("\nPlease enter years of investment"))
                monthly_repayment = (interest_rate * house_value)/(1- (1 + interest_rate)**(-repay_month))
                print(f"\nYour monthly repayment within the specified duration is {monthly_repayment}")
                break  
            except:
                print("Error, Please enter a numberic character only")    
            continue     
            
      else: 
          print("Your input is invalid, Pleas input correct option")