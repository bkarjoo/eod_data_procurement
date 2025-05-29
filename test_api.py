import requests
import gzip
import io

def download_and_save(url, params, filename):
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.content

    # Check if content is gzipped by magic number
    if data[:2] == b'\x1f\x8b':
        print("Data is gzip compressed. Saving as", filename + ".gz")
        with open(filename + ".gz", "wb") as f:
            f.write(data)
    else:
        print("Data is not compressed. Saving as", filename)
        with open(filename, "wb") as f:
            f.write(data)

if __name__ == "__main__":
    url = "http://127.0.0.1:8085/download_ohlc"
    params = {
        "symbols": "AAPL,MSFT",
        "start_date": "2024-01-01",
        "end_date": "2024-03-31"
    }
    download_and_save(url, params, "ohlc_data")
