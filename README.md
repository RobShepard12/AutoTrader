# AutoTrader
Theoretical auto trader for crypto based on historical data

Goal: enhance the method of buying/selling to have a stronger profit margin 
and have the program use this method to automatically make real world trades 
through attaching it to a trading platform for real profits.

Different possible methods:
1) (currently implemented) if there is a X% dip (X can be changed to desired %) from the previous data point buy then hold until there is X profit
   (more transactions, smaller profit per sell, less risky, do not buy if there has been Y consecutive dips (needs to be implemented) )
   
2) buy within 10% of previous months lowest then hold until there is an X profit and sells, repeats 
   (fewer transactions, larger profit per sell, high risk) 
   
3) if the price of the coin is less by X amount of the coins price the previous hour and is not a certain % below the past 30 days buy coin
   if the comparison between the buy and the current coin value is X profit buy the coin.
