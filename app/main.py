from typing import Optional
from fastapi import FastAPI, Header, Request
import logging

logging.basicConfig(filename='log/logger.log', encoding='utf-8', level=logging.INFO)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/line")
async def callback(request: Request, x_line_signature: Optional[str] = Header(None)):
    body = await request.body()
    logging.info(f'x_line_signature header = {x_line_signature}')
    logging.info(f'body = {body}')
    return "ok"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}