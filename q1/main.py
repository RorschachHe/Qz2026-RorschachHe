import json


def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }

    try:
        f = open(filepath, "r", encoding="utf-8")
    except FileNotFoundError:
        return result

    for line in f:
        line = line.strip()

        if line == "":
            continue

        try:
            log = json.loads(line)
        except json.JSONDecodeError:
            
            continue

        result["total"] += 1

        level = log["level"]
        user = log["user"]
        message = log["message"]

        if level in result["by_level"]:
            result["by_level"][level] += 1
        else:
            result["by_level"][level] = 1

        if user in result["by_user"]:
            result["by_user"][user] += 1
        else:
            result["by_user"][user] = 1

        if level == "ERROR":
            result["last_error"] = message

    f.close()
    return result

# 运行main.py文件
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print(analyze_log(sys.argv[1]))
    else:
        print("请传入 jsonl 文件路径，例如：python main.py my.jsonl")