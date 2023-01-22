import pandas as pd
import time
from itertools import product

# Load data from .csv file
global_data = []



'''
data2 = pd.read_csv('BTC-USD.csv')
previous_close = 22321.765625
global_data.append((" BTC ",data2,previous_close))
'''


'''
#print(" =============       2023 SIMULATION         =============")     
data2 = pd.read_csv('SP500_2023.csv')
previous_close = 3824.14 
global_data.append((" 2023 ",data2,previous_close))

'''
#print(" =============       2 MONTHS SIMULATION         =============")       
data1 = pd.read_csv('SP500_2mo.csv')
previous_close = 3856.1
global_data.append(("2 months",data1,previous_close))

'''
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

combinations = list(product(["long", "short"], repeat=6))
combinations2 = list(product([1,2,3],repeat=4))
proo = -100
scenario = 0
coms = 0
for combination in combinations:
    var1, var2, var3, var4, var5, var6 = combination
    
    for com in combinations2:
        num3,num4,num7,num8 = com
    
        for d in global_data :
            timeline = d[0]
            data = d[1]
            previous_close = d[2]
            #print("\n")
            #print("=======      "+timeline+"        =======")

            data = data.iloc[::-1]
            # Initialize variables
            initial = 500
            profit = 0
            leverage = 50
            invested = 0 
            starter = initial
            portfolio_value = initial + invested + profit # starting portfolio value
            stop_loss = 0.1 # stop loss and take profit at 10% of portfolio value
            position = "None" # current position (long or short)
            previous_position = "None"
            previous_profit = 0
            #previous_close = 2776.42 # 3994.07 
            variability = 0
            trades = 0
            initial_price = previous_close
            global_positive = 0
            global_negative = 0
            positive = 0
            negative = 0
            coef = 1
            hold_days = 0

            
            def open_position(pos, previous_pos):
                close_position()
                global position, previous_position, initial, trades, coef, invested, profit, initial_price
                if pos == "short" : coef = -1
                else : coef = 1
                position = pos
                previous_position = previous_pos
                invested = initial 
                initial = 0
                profit = 0
                initial_price = close
                trades += 1
                #print(str(date) + " > open "+pos+" position :  INVESTED = " + str(int(invested)))

                
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
                    #print(str(date) + " > close "+previous_position+" position :  PROFIT = " + str(int(previous_profit)))


            # Loop through data
            for i, row in data.iterrows():
                date = row['Date']
                #close = row['Close'].replace(',','').astype(float)
                close = pd.to_numeric(row['Close'], errors='coerce')
                percentage = (100 - (initial_price / close) * 100)/100*leverage
                profit = invested * percentage * coef
                variability = variability + abs(close - previous_close)    
                portfolio_value = initial + invested + profit
                
                if position == "None":
                    hold_days = 0
                else :
                    hold_days += 1
                
                '''
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
                '''
                if int(portfolio_value) <= 0 :
                        break

                if percentage > 0 :
                    global_positive += 1
                    negative = 0
                    positive += 1
                    
                    if position == "None":
                        if positive <= 1 :
                            #open_position("long","None")
                            open_position(var1,"None")
                        elif positive >= 3 :
                            #open_position("short","None")
                            open_position(var2,"None")
                    elif position == "long":
                        close_position()
                        if positive >= num3 :
                            #open_position("short","None")
                            open_position(var3,"long")
                    elif position == "short":
                        if positive >= num4 and percentage >= 0.2:
                            close_position()
                            
                            #open_position("long","short")
                    #elif position == "short" :
                    #    close_position("short")
                        
                    
                elif percentage < 0 :
                    global_negative += 1
                    positive = 0
                    negative += 1
                    
                    if position == "None":
                        if negative <= 1 :
                            #open_position("long","None")
                            open_position(var4,"None")
                        elif negative >= 1 :
                            #open_position("long","None")
                            open_position(var5,"None")
                    elif position == "short":
                        close_position()
                        if negative >= num7 :
                            #open_position("long","None")
                            open_position(var6,"short")
                    elif position == "long":
                        if  negative >= num8 and percentage <= -0.2:
                            close_position()
                            
                            
                            #open_position("short","long")
                    #elif position == "long" :
                    #    close_position("long") 
                
                    
                    
                previous_percentage = percentage
                portfolio_value = initial + invested + profit
                previous_close = close

                #time.sleep(2)

            '''
            print(" Initial : $" + str(starter))
            print(" Profit  : $" + str(int(portfolio_value) - starter))
            print(" Portfolio : $" + str(int(portfolio_value)))
            print(" Variability Cash : $" + str(int(variability)))   
            percentage_var = ((int(portfolio_value) - starter)/ variability) * 100
            print(" Success Rate : {:.2f} %".format(percentage_var))
            print(" Growth : {:.2f} %".format(((portfolio_value-starter) / starter)*100))
            print(" Next Move : " + position)
            print(" Number of trades : " + str(trades))
            print(" Positive : " + str(global_positive))
            print(" Negative : " + str(global_negative))
            '''
        if proo < int(portfolio_value) - starter:
            proo =  int(portfolio_value) - starter
            scenario = combination
            coms = com
            
print(" Top Profit : " + str(proo) + " = combination : " + str(scenario) + " " + str(coms))



    