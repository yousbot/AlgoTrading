import pandas as pd
import time
from itertools import product
from datetime import datetime
from termcolor import colored

# Load data from .csv file
global_data = []

print("\n")

# Uncomment only one csv file, depending on the period you want to simulate

data2 = pd.read_csv('BTC-USD.csv')
previous_close = 22321.765625
global_data.append((" BTC ",data2,previous_close))


'''
#print(" =============       2023 Personal Projection       =============")     
data2 = pd.read_csv('SP500_future.csv')
previous_close = 3897.57
global_data.append((" 2023 ",data2,previous_close))


#print(" =============       2023 SIMULATION         =============")     
data2 = pd.read_csv('SP500_2023.csv')
previous_close = 3824.14 
global_data.append((" 2023 ",data2,previous_close))


#print(" =============       2 MONTHS SIMULATION         =============")       
data1 = pd.read_csv('SP500_2mo.csv')
previous_close = 3856.1
global_data.append(("2 months",data1,previous_close))

#print(" =============       5 MONTHS SIMULATION         =============")       
data1 = pd.read_csv('SP500_5mo.csv')
previous_close = 4155.38
global_data.append(("5 months",data1,previous_close))


#print(" =============       1 YEAR SIMULATION         =============")     
data2 = pd.read_csv('SP500_1year.csv')
previous_close = 1472.63 
global_data.append(("1 year",data2,previous_close))

#print(" =============       2 YEARS SIMULATION         =============")      
data3 = pd.read_csv('SP500_2years.csv')
previous_close = 3055.73 
global_data.append(("2 years",data3,previous_close))


#print(" =============       5 YEARS SIMULATION         =============")      
data4 = pd.read_csv('SP500_5years.csv')
previous_close = 2776.42
global_data.append(("5 years",data4,previous_close))

#print(" =============       10 YEARS SIMULATION         =============")      
data5 = pd.read_csv('SP500_10years.csv')
previous_close = 1472.63
global_data.append(("10 years",data5,previous_close))
'''

for d in global_data :
    timeline = d[0]
    data = d[1]
    previous_close = d[2]
    data = data.iloc[::-1]
    
    ## Static Wallet Settings
    leverage = 20 # Leverage

    ## Dynamic Wallet
    initial = 500 # Current Cash
    starter = initial # Initial deposit
    profit = 0
    previous_profit = 0
    invested = 0 
    portfolio_value = initial + invested + profit
    position = "None" # current position (long or short or None)
    previous_position = "None"

    ## Performance Variables
    variability = 0 # cummulative change of SP500 Price day to day 
    trades = 0 # number of trades made by Bot
    initial_price = previous_close
    global_positive = 0 # number of times stock went up
    global_negative = 0 # number of times stock went down
    positive = 0 # becomes 0 if stock changes position
    negative = 0 # becomes 0 if stock changes position
    coef = 1 
    hold_days = 0 # diamond hands days
    previous_month = 11
    
    ## Open Position
    def open_position(pos, previous_pos):
        global position, previous_position, initial, trades, coef, invested, profit, initial_price  
        close_position()
        if pos == "short" : coef = -1
        else : coef = 1
        position = pos
        previous_position = previous_pos
        invested = initial 
        initial = 0
        profit = 0
        initial_price = close
        trades += 1
        color = "blue"
        print(" | " + str(date) + " : Open " + pos + " position. Invest : " + colored("$ "+str(int(invested)),color))

    ## Close Position
    def close_position():
        global invested, profit, initial, coef, portfolio_value, position, previous_position, hold_days
        if position != "None":
            hold_days = 0
            previous_position = position
            position = "None"
            initial = portfolio_value
            previous_profit = profit
            profit = 0
            invested = 0
            color = "green" if int(previous_profit) > 0 else "red"
            print(" | " + str(date) + " : Close " + previous_position + " position. Profit : " + colored("$ "+str(int(previous_profit)),color))

    ## Reset Wallet
    def reset_wallet():
        global positive, negative, hold_days, previous_position, coef
        close_position()
        positive = negative = hold_days = coef = 0 
        previous_position = "None"
        print(colored(" | Wallet reset. ","blue"))
        
    # Loop through data
    for i, row in data.iterrows():
        date = row['Date']
        
        ## Calculating Wallet Values
        close = pd.to_numeric(row['Close'], errors='coerce')
        percentage = (100 - (initial_price / close) * 100)/100*leverage
        profit = invested * percentage * coef
        variability = variability + abs(close - previous_close)    
        portfolio_value = initial + invested + profit
        if position == "None":
            hold_days = 0
        else :
            hold_days += 1
        
        ## Print Details of Each Day ( comment this if you don't want output of Days )
        ## Useful to follow positions and understand process
        """
        print(" # Date : " + str(date) )
        print("         > Close / Prev : " + str(close) + " / " + str(previous_close))
        print("         > Initial : " + str(int(initial)))
        print("         > Profit  : " + str(int(profit)))
        print("         > Invested : " + str(int(invested)))
        print("         > Portfolio Value : " + str(int(portfolio_value)))
        print("         > Variation {:.2f} %".format(percentage*100))
        print("         > Current Position : " + position)
        print("         > Initial Opening : " + str(initial_price))
        print("         > hold Days : " + str(hold_days))
        """
        ## In case we lost everything
        if int(portfolio_value) <= 0 :
                break
            
        ## If stock is going UP
        if percentage > 0 : 
            
            # Performance 
            global_positive += 1    # positives +1
            positive += 1           # current positive trend +1
            negative = 0            # previous negative trend no longer here

            if position == "None":
                if positive <= 1 :
                    open_position("long","None")
                elif positive >= 3 :
                    open_position("short","None")
            elif position == "long":
                close_position()
                if positive >= 3 :
                    open_position("long","long")
            elif position == "short":
                if positive >= 3 and percentage >= 0.2:
                    close_position()              
                
        ## If stock is going DOWN
        elif percentage < 0 :
            
            # Performance
            global_negative += 1    # negatives +1
            negative += 1           # current negative trend +1
            positive = 0            # previous positive trend no longer here
            
            if position == "None":
                if negative <= 1 :
                    open_position("long","None")
                elif negative > 1 :
                    open_position("long","None")
            elif position == "short":
                close_position()
                if negative >= 2 :
                    open_position("long","short")
            elif position == "long":
                if negative >= 3 and percentage <= -0.2:
                    close_position()
                    
        ## Archive settings
        previous_percentage = percentage
        portfolio_value = initial + invested + profit
        previous_close = close

        #time.sleep(2)

    ## You can print this view only to see the global performance
    print("\n")
    print(" Initial Deposit     : $ " + str(starter))
    color = "green" if int(portfolio_value) - starter > 0 else "red"
    print(" Profit              : "+colored("$ "+str(int(portfolio_value) - starter),color))
    color = "green" if int(portfolio_value) > 0 else "red"
    print(" Portfolio           : "+colored("$ " + str(int(portfolio_value)),color))
    color = "green" if ((portfolio_value-starter) / starter)*100 > 0 else "red"
    print(" Growth              : "+colored("% {:.2f}".format(((portfolio_value-starter) / starter)*100),color))
    print(" Next Move           : " + position)
    print(" Number of trades    : " + str(trades))
    print(" Positive            : " + str(global_positive))
    print(" Negative            : " + str(global_negative))
    print("\n")

