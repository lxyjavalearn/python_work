
# 问题一：创建一个python类怎么创建结构是什么 也是逐行运行吗

# 解析一个json
import json

# 写JSONL
data = [{"text": "你好", "label": 0}, {"text": "不好", "label": 1}]
with open("data.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# 读JSONL
loaded = []
with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        loaded.append(json.loads(line))
print(loaded)