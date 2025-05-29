from data_loader import load_ohlc_compressed_csv

db_path = 'eod2.db'
symbols = ['AAPL', 'MSFT']
start_date = '2024-01-01'
end_date = '2024-03-31'

compressed_csv = load_ohlc_compressed_csv(db_path, symbols, start_date, end_date)

print(f'Compressed data size: {len(compressed_csv)} bytes')

# Optional: decompress and preview first 500 chars
import gzip
import io

with gzip.GzipFile(fileobj=io.BytesIO(compressed_csv), mode='rb') as f:
    decompressed = f.read().decode('utf-8')

print(decompressed[:500])
