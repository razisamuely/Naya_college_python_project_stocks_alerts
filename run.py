import pandas as pd
import yfinance as yf


def get_stock_closing_prices(stocks, start_date, end_date):
    data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
    return data


days_back_interval = 60


# Define the stocks and dates
stocks = ['NVDA', 'AMD', 'AVGO', 'INTC', 'ARM']
start_date = pd.Timestamp.now() - pd.Timedelta(days=days_back_interval)
end_date = pd.Timestamp.now()

# Fetch closing prices
closing_prices = get_stock_closing_prices(stocks, start_date, end_date)

scalled = closing_prices / closing_prices.iloc[0,:]


days_back_avg  = 3
scalled_avg = scalled.rolling(days_back_avg).mean()


def get_most_correlated_stocks(df,target_stock,number_of_top):
    return df.corr().sort_values(by = target_stock, ascending = False).iloc[1:number_of_top + 1 ][[target_stock]].to_dict()



target_stock = "NVDA"
most_correlated = get_most_correlated_stocks(df = scalled_avg,
                                             target_stock = "NVDA",
                                             number_of_top = 3)

most_correlated = list(most_correlated[target_stock].keys())


last_2_days = closing_prices[most_correlated].tail(2)
change_last_2_days = (last_2_days.iloc[1,:] -last_2_days.iloc[0,:]) /last_2_days.iloc[0,:]

threshold = 0.02
rais_exception = abs(change_last_2_days) > threshold

def run(target_stock,stocks):
    closing_prices = get_stock_closing_prices(stocks, start_date, end_date)
    scalled = closing_prices / closing_prices.iloc[0,:]
    scalled_avg = scalled.rolling(days_back_avg).mean()
    most_correlated = get_most_correlated_stocks(df = scalled_avg,
                                                      target_stock = target_stock,
                                                      number_of_top = 3)
    most_correlated = list(most_correlated[target_stock].keys())

    last_2_days = closing_prices[most_correlated].tail(2)
    change_last_2_days = (last_2_days.iloc[1,:] -last_2_days.iloc[0,:]) /last_2_days.iloc[0,:]
    rais_exception = abs(change_last_2_days) > threshold
    return rais_exception




target_stock = "NVDA"
stocks = ['NVDA', 'AMD', 'AVGO', 'INTC', 'ARM',"QCOM", "MU", "TXN", "NXPI","CSCO"]
while True :
    for target_stock_name in stocks:
        rais_exception = run(target_stock = target_stock_name,stocks=stocks)
        print(f"results for {target_stock_name} \n" ,rais_exception)
    time.sleep(10)
    






