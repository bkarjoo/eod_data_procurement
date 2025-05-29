from data_loader import load_ohlc_filtered

db_path = 'eod2.db'
symbols = ['AAPL', 'MSFT']
start_date = '2024-01-01'
end_date = '2024-03-31'

df = load_ohlc_filtered(db_path, symbols, start_date, end_date)
print(df.head())
print(df.tail())
print(f'Total rows: {len(df)}')
