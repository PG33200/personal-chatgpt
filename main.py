from fastapi import FastAPI
from GodChatGPT import GodChatGPT
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"hello":"word"}

@app.get("/test")
def run_bot(query: str):
    god_chatgpt = GodChatGPT()
    result = god_chatgpt.agent_executor({"input": query})
    print(result)
    return {"result":result['output']}