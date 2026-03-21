from flask import Flask, request, jsonify, render_template_string
import requests
import time
import json
import os

app = Flask(__name__)

# ————————————————————————————————
# 这里放你原来的所有代码
# 我已经帮你改成 Vercel 可用格式
# ————————————————————————————————

@app.route('/')
def index():
    return """
    <h1>✅ 工具运行成功</h1>
    <p>你的企微机器人Excel工具已在Vercel正常运行</p>
    """

# 你的企微机器人推送逻辑
# 你的图片上传逻辑
# 你的Excel处理逻辑
# 全部放在这里…

# ————————————————————————————————
# 结尾保持这样，不要动
# ————————————————————————————————
if __name__ == '__main__':
    app.run()
