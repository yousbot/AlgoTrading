
# S&P500 Market Simulation

This project provides a tool for simulating the performance of the S&P500 market using historical data and different trading strategies.

## Rules

* You can open one position per day
* You can open one position at a time ( to open you need to close )
* Your function is to maximize profit 
* You can use any historical data of any market, with the csv file having to have two columns ( Date / Close ) 
* **close** refers to the price of the closing market each day*

## Features

* Simulation of the S&P500 market performance over different periods of time (2023 Personal Projection)
* Different trading strategies and parameters, such as leverage and long/short positions
* Tracking of key performance metrics such as number of trades, total profit/loss, and percentage change in the index

## Requirements

* Python 3.x
* Pandas, NumPy, and Matplotlib (for data analysis and visualization)
* termcolor (for colored output)


## Usage/Examples

**Find settings of your market :** 

First step is to launch the bruteforce search to find the optimum settings to be used for the market and historical data of your choice.
```shell
python settings_bruteforce_SP500.py
```

this will check all the possible settings, for the SP500 market using historical data we provided in the begining of the script.
Its goal is to find the possible combinations that will secure the most profit in that period, for the following variables : 

```python
var1,var2,var3,var4,var5,var6,num1,num2,num3,num4,num5,num6
```

Once the script finishes, the result you get is as follow :
```python
# Example of 2023 period ( first 18 days ) 
Top Profit : $644 = combination : ('short', 'long', 'short', 'long', 'long', 'long') (1, 3, 2, 1, 1, 1, 1, 1)
# Example of 2 months period of SP500 ( November 22 -> January 23 )
Top Profit : $17791 = combination : ('long', 'short', 'long', 'long', 'long', 'long') (1, 3, 3, 1, 1, 1, 2, 3)
# Example of 1 year period ( first 18 days ) 
Top Profit : $156119 = combination : ('long', 'short', 'long', 'long', 'short', 'long') (1, 3, 3, 3, 1, 1, 2, 3)
# Example of 2 years period ( first 18 days ) 
Top Profit : $5576 = combination : ('long', 'short', 'long', 'short', 'long', 'long') (1, 3, 2, 2, 1, 1, 2, 3)

```
The script used simulates a usage of $500 deposit, leveraged at 20.

**Simulate the historical data**

Once you have your historical data prepared, and your settings of the var & num variables ready. Change the simulation script accordingly.

```shell
python simulation_sp500.py
```

this will go through the historical data and simulate a day to day trading, knowingly you make one trade at a time and in a day.
The result will look as follow ( tested on first 18 days of 2023 SP500 market ): 

```shell
 | 01/04/23 : Open long position. Invest : $ 500
 | 01/06/23 : Close long position. Profit : $ 108
 | 01/10/23 : Open short position. Invest : $ 608
 | 01/11/23 : Close short position. Profit : $ -154
 | 01/12/23 : Open short position. Invest : $ 453
 | 01/18/23 : Close short position. Profit : $ 125
 | 01/19/23 : Open long position. Invest : $ 579


 Initial Deposit     : $ 500
 Profit              : $ 79
 Portfolio           : $ 579
 Growth              : % 15.86
 Next Move           : long
 Number of trades    : 4
 Positive            : 8
 Negative            : 3
```

All the positions opened as well as the overall performance of your portfolio in that period.

More details can be found in the script.

## Data

The data used in this simulation is based on historical data of the S&P500 index, you can find the data in the project files of different periods, from 10 years to 18 days in 2023.

## Additional information

* The script is using the following trading strategy:

        Long position strategy: Buy when the market is going up, and sell when the market is going down.
        Short position strategy: Short when the market is going down, and cover when the market is going up.
* The script tracks the following performance metrics:

        Number of trades
        Total profit/loss
        Percentage change in the index
        Number of positive and negative days
        Number of hold days


# S&P500 Market Simulation

This project provides a tool for simulating the performance of the S&P500 market using historical data and different trading strategies.

## Features

* Simulation of the S&P500 market performance over different periods of time (2023 Personal Projection)
* Different trading strategies and parameters, such as leverage and long/short positions
* Tracking of key performance metrics such as number of trades, total profit/loss, and percentage change in the index

## Requirements

* Python 3.x
* Pandas, NumPy, and Matplotlib (for data analysis and visualization)
* termcolor (for colored output)


## Authors

- [Youssef Sbai Idrissi ( LinkedIn )](linkedin.com/sbaiidrissiyoussef?_l=en_US)

