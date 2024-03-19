import yfinance as yf
import matplotlib.pyplot as plt 

class utils():
    def __init__(self):
        pass 
        
    def _get_stock_closing_prices(self,stocks, start_date, end_date):
        data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']
        return data
            
    def _get_most_correlated_stocks(self,df,target_stock,number_of_top):
        return df.corr().sort_values(by = target_stock, ascending = False).iloc[1:number_of_top + 1 ][[target_stock]].to_dict()
    
    def _save_plot(self, df):
        plt.figure(figsize = (5,5)) 

        plt.plot(df);
        plt.legend(list(df.columns));
        
        plt.savefig("raz.png")

    def run(self,target_stock,stocks, start_date, end_date, days_back_avg ,threshold):
        closing_prices = self._get_stock_closing_prices(stocks, start_date, end_date)
        scalled = closing_prices / closing_prices.iloc[0,:]
        scalled_avg = scalled.rolling(days_back_avg).mean()
        self._save_plot(df = scalled_avg)
        most_correlated = self._get_most_correlated_stocks(df = scalled_avg,
                                                          target_stock = target_stock,
                                                          number_of_top = 3)
        most_correlated = list(most_correlated[target_stock].keys())
    
        last_2_days = closing_prices[most_correlated].tail(2)
        change_last_2_days = (last_2_days.iloc[1,:] -last_2_days.iloc[0,:]) /last_2_days.iloc[0,:]
        rais_exception = abs(change_last_2_days) > threshold
        return rais_exception
    
    
