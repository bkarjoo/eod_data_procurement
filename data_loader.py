import gzip
import io
import sqlite3

import pandas as pd


def load_ohlc_filtered(db_path, symbols, start_date, end_date):
    placeholders = ','.join('?' for _ in symbols)
    query = f'''
    SELECT Date, Symbol, ExchangeOpen, OfficialClose, AdjustedClose, Volume, ExchangeOpenSize
    FROM ohlc
    WHERE Symbol IN ({placeholders})
      AND Date BETWEEN ? AND ?
    '''
    params = symbols + [start_date, end_date]
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn, params=params)
    return df



def load_ohlc_compressed_csv(db_path, symbols, start_date, end_date):
    placeholders = ','.join('?' for _ in symbols)
    query = f'''
    SELECT Date, Symbol, ExchangeOpen, OfficialClose, AdjustedClose, Volume, ExchangeOpenSize
    FROM ohlc
    WHERE Symbol IN ({placeholders})
      AND Date BETWEEN ? AND ?
    '''
    params = symbols + [start_date, end_date]
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn, params=params)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    compressed_buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_buffer, mode='wb') as gz_file:
        gz_file.write(csv_buffer.getvalue().encode('utf-8'))
    return compressed_buffer.getvalue()
