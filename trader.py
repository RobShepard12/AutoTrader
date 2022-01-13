"""
Author: Robert Shepard
Description: trader to take in any crypto price data and automatically trade for profit
Currently setup for ethereum
"""
import csv

usd = 1000
purchases = []
buy_amount= 50 #USD

def make_money(list, average):
    """
    this buys at a certain value under the average and holds until there is a guarantee profit, so there is no losing money
    """
    #list = hourly prices over 1 week
    #average = average over 1 week
    global usd
    total_profit = 0
    total_usd_received = 0
    for price in list: 
        print(f"Analyzing price: {price}")
        num = average * .005
        if price < (average - num): 
            buy_coin(price)
            print(f"Bought coin at: {price}")
        elif price > (average + num):
            if len(purchases) != 0:
                invested = 0
                for i in purchases:
                    invested += buy_amount
                profit = process_profits(price) #profit from series of sells
                total_profit += profit #straight profit disregarding amount bought
                entire_sell_price = invested + profit #$50 + RAW profit
                total_usd_received += entire_sell_price
                print(f"total usd received: {total_usd_received}\n")
                purchases.clear()
            else:
                print("Holding, price is climbing and do not hold any coin")
                #coin is climbing but do not hold any portion of coin
        else:
            pass #hold onto coin
    
    usd += total_usd_received
    return usd, total_profit



def process_profits(sell_price):
    """
    goes through all coin values and plugs them into sell coin function
    returns total PROFIT from series of sells
    """
    profit = 0
    print("\n**SELLING PURCHASES**")
    print(f"Purchase Prices: {purchases}")

    for buy_price in purchases:
        singular_profit = sell_coin(buy_price, sell_price)
        profit += singular_profit

    print(f"Total profit from series of sell: {profit}")
    
    return profit

def sell_coin(buy_price, sell_price):
    #sells one individual purchase
    print(f"Buy price: {buy_price}")
    print(f"Sell price: {sell_price}")

    difference = round(sell_price - buy_price, 3)
    print(f"Difference: {difference}")

    profit_percentage = round((difference / buy_price), 3) #percentage profit of each sell
    print(f"Profit margin: {profit_percentage}")

    singular_profit = round((buy_amount * profit_percentage), 3) #profit from each sell
    print(f"Singular Profit: {singular_profit}")

    print(f"Sell amount: {buy_amount + singular_profit}")
    return singular_profit
    

def take_in_file(file):
    """
    Takes in file and process data to a readable format
    """
    distance = 20 #how many closing prices you want to analyze based on the csv used
    with open(file) as csv_file:
        closing_prices = []
        i=0
        csv_reader = csv.reader(csv_file)
        next(csv_reader) #skips descriptor row
        for line in csv_reader:
            closing_prices.append(float(line[6])) #line[6] = closing prices
            i+=1
            if i >= distance: 
                break
    return closing_prices

def get_average(list):
    num_items = 0
    total = 0
    for i in list:
        num_items+=1
        total += i
    average = total/num_items
    return average


def detect_lows(data):
    """
    look through data
    find lowest previous month
    find low within X% of that price
    call buy function
    """
    #will be implemented for real world trading
    pass

def buy_coin(price):
    """
    buy coin when called (have special case if it dips really low buy more)
    document what bought at, subtract that from USD
    """
    global usd
    usd -= buy_amount
    purchases.append(price)
    print(f"USD: {usd}")
    

def main():
    #eth:
    hourly = 'C:\\Users\\rober\\OneDrive\\Desktop\\eth\\ETH_1H.csv' #price hourly
    minute = 'C:\\Users\\rober\\OneDrive\\Desktop\\eth\\ETH_1min.csv' #price every minute
    daily =  'C:\\Users\\rober\\OneDrive\\Desktop\\eth\\ETH_day.csv' #price daily

    file_path = f"{hourly}"
    
    prices = take_in_file(file_path) #gets closing prices
    average = get_average(prices) #gets average of closing prices
    print(f"Average: {average}")
    total_profit = make_money(prices, average) #main run function
    print(f"Total USD: {total_profit[0]}, Total profit: {total_profit[1]}")

if __name__ == "__main__":
    main()