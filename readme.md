# EOD Data Procurement

## Setup

1. Place your Google API `credentials.json` in the project root.

2. Run the downloader to fetch the latest database:

   ```bash
   python download_db.py
   ```

## API Usage

Start the API server:

```bash
uvicorn api:app --reload --port 8085
```

Call the endpoint with parameters:

```
GET /download_ohlc?symbols=AAPL,MSFT&start_date=2024-01-01&end_date=2024-03-31
```

The response is a gzip-compressed CSV file.

## Sample Consumer

`test_api.py`