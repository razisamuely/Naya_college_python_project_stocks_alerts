import pandas as pd
import yfinance as yf
import argparse
import time 

from utils import utils
        
def run_all(target_stock, days_back_avg, days_back_interval, threshold, stocks:str):
    utl = utils()

    
    stocks = stocks.split(",")
    # Define the stocks and dates
    start_date = pd.Timestamp.now() - pd.Timedelta(days=days_back_interval)
    end_date = pd.Timestamp.now()


    while True :
        for target_stock_name in stocks:
            rais_exception = utl.run(target_stock = target_stock_name,stocks=stocks, 
                                     start_date= start_date, 
                                     end_date = end_date, 
                                     days_back_avg=days_back_avg , 
                                     threshold = threshold)
                
            print(f"results for {target_stock_name} \n" ,rais_exception)
        time.sleep(10)
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stocks")
    parser.add_argument("--target_stock", type=str, help="The number to calculate square and cube for")
    parser.add_argument("--days_back_avg", type=int, help="")
    parser.add_argument("--days_back_interval", type=int, help="")
    parser.add_argument("--threshold", type=float, help="")
    parser.add_argument("--stocks", type=str, help="")

    
    args = parser.parse_args()
    run_all(target_stock = args.target_stock,
           days_back_avg = args.days_back_avg,
           days_back_interval = args.days_back_interval,
           threshold = args.threshold,
           stocks = args.stocks)

