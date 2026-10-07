from main import analyze_log

# 文件不存在
print(analyze_log("not_exist.jsonl"))

# 手动创建一个测试文件
with open("app.jsonl", "w", encoding="utf-8") as f:
    f.write('{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "ok", "user": "张三"}\n')
    f.write('{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "失败", "user": "李四"}\n')

print(analyze_log("app.jsonl"))