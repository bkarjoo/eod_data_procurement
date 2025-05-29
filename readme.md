# EOD Data Procurement

## Setup

1. Clone the repo and create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your Google API `credentials.json` in the project root.

4. Run the downloader to fetch the latest database:

   ```bash
   python download_db.py
   ```

## API Usage

Start the API server:

```bash
uvicorn api:app --reload
```

If port 8000 is in use, you can specify a different port:

```bash
uvicorn api:app --reload --port 8085
```

Call the endpoint with parameters:

```
GET /download_ohlc?symbols=AAPL,MSFT&start_date=2024-01-01&end_date=2024-03-31
```

The response is a gzip-compressed CSV file.

## Sample Consumer

Use `test_api.py` to download and save the compressed CSV:

```bash
python test_api.py
```

---

Want me to add or modify anything?
