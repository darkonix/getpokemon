from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import random
import uvicorn
import os
import json

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    r_id = random.randint(1, 1000)
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{r_id}")
    # ans = json.loads(r.json())
    # ans['id'] = r_id
    # return json.dumps(ans)
    return r.json()

@app.get("/list/")
async def get_list(q: list | None = Query()):
    film_list = []
    for id in q:
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        film_list.append(r.json())
    return film_list

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))

