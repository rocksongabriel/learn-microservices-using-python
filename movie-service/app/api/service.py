import os

import httpx
from dotenv import load_dotenv

load_dotenv()

client = httpx

CAST_SERVICE_HOST_URL = "http://localhost:8002/api/v1/casts/"
casts_url = os.getenv("CAST_SERVICE_HOST_URL") or CAST_SERVICE_HOST_URL


def is_cast_present(cast_id: int):
    response = client.get(f"{casts_url}{cast_id}")
    return True if response.status_code == 200 else False
