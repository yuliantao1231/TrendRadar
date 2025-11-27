import os
import datetime
import json

# 1. 假设你的爬虫产出都在 news_list 变量，为 list[dict]，每条有唯一 id 或 url 字段
# 2. 推送逻辑用 send_notification(news) 或 send_ntfy(news) 实现

def load_pushed_ids(today):
    push_log_file = f"push_log_{today}.json"
    if os.path.exists(push_log_file):
        with open(push_log_file, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_pushed_ids(today, pushed_ids):
    push_log_file = f"push_log_{today}.json"
    with open(push_log_file, "w", encoding="utf-8") as f:
        json.dump(list(pushed_ids), f, ensure_ascii=False)

def main():
    # 你的实际新闻抓取逻辑
    news_list = crawl_news()   # 这里换成你真实的爬虫返回新闻列表

    # 字段唯一标识可以用 news['url'] 或 news['id']
    today = datetime.date.today().isoformat()
    pushed_ids = load_pushed_ids(today)

    # 去重
    unique_news = []
    seen = set(pushed_ids)
    for news in news_list:
        key = news.get('url') or news.get('id') or hash(str(news))
        if key not in seen:
            unique_news.append(news)
            seen.add(key)
        if len(unique_news) >= 100:
            break   # 最多100条

    # 批量推送
    for news in unique_news:
        # 你的推送代码，例如 send_ntfy(news)
        # send_ntfy(news)
        pass

    # 记下已推送
    pushed_ids.update([(n.get('url') or n.get('id')) for n in unique_news])
    save_pushed_ids(today, pushed_ids)

def crawl_news():
    # TODO: 你的新闻爬取实现
    # 返回格式: list[dict]，每条dict有 url 和/或 id 字段
    return []

if __name__ == "__main__":
    main()
