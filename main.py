from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ⚠️ 允许你的 GitHub Pages 域名访问，开发时可先写 "*"
origins = [
    "*",
    "http://127.0.0.1:5500",  # 本地预览用
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"msg": "Python 后端运行中！"}

@app.get("/api/hello")
def say_hello(name: str = "世界"):
    return {"greeting": f"你好, {name}！来自 Python 后端"}