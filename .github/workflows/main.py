import json
import os

# 1. 尝试读取去重文件，如果没有就用空集
rec_file = ".pushed_ids.json"
if os.path.exists(rec_file):
    with open(rec_file, "r", encoding="utf-8") as f:
        pushed_ids = set(json.load(f))
else:
    pushed_ids = set()

# 2. 假定你新的新闻列表变量叫 news_list，里面每条有 news['url'] 作为唯一id
news_list = crawl_news()  # 实际中你用你自己的爬虫生成它

# 3. 去重+限制100条
to_push = []
for news in news_list:
    news_id = news['url']   # 或 news['id']
    if news_id not in pushed_ids:
        to_push.append(news)
        pushed_ids.add(news_id)
    if len(to_push) >= 100:
        break

# 4. 推送逻辑
for news in to_push:
    send_notification(news)  # 用你自己的推送函数

# 5. 保存去重记录（覆盖原文件）
with open(rec_file, "w", encoding="utf-8") as f:
    json.dump(list(pushed_ids), f, ensure_ascii=False, indent=2)

print(f"今日实际推送{len(to_push)}条新闻")
