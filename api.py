from fastapi import FastAPI, Query, Response
from fastapi.responses import StreamingResponse
import io
from data_loader import load_ohlc_compressed_csv  # adjust if filename differs

app = FastAPI()

@app.get("/download_ohlc")
def download_ohlc(
    symbols: str = Query(..., description="Comma-separated symbols"),
    start_date: str = Query(...),
    end_date: str = Query(...)
):
    symbol_list = symbols.split(",")
    compressed_data = load_ohlc_compressed_csv("eod2.db", symbol_list, start_date, end_date)
    return Response(
        content=compressed_data,
        media_type="application/gzip",
        headers={
            "Content-Disposition": f"attachment; filename=ohlc_{start_date}_to_{end_date}.csv.gz"
        }
    )
