THis a start.
选择题：
1. B 2. B 3. B 4. B 5. B 6. B 7. B 8. B 9. B 10. B

简答题：
1.  a和b共享同一个list，b为浅拷贝，c是一个新list，将a中的元素复制到c中，二者独立互不影响
    执行后，a和b的第一个list添加元素'99'，而c不发生改变

2.  1. `error_logs = [log for log in logs if log["level"] == "ERROR"]`
    2. 
    ```
    user_counts = {}
    for log in logs:
        user = log["user"]
        user_counts[user] = user_counts.get(user, 0) + 1
    ```
    3. `len(logs)` 只能得到log总数目，无法计算用户出现次数

3.  ```
    def safe_divide(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError):
        return None
    ```
    代码更易读，可以直接针对目标情况进行判断，if语句需要避免工作情况或是特例


