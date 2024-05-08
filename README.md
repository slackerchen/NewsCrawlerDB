# NewsCrawlerDB

---


## 项目描述
这个项目是一个新闻爬虫，它可以从百度新闻搜索中抓取与指定关键词相关的新闻标题、链接、来源和日期，并将这些数据存储到MySQL数据库中。这个项目是为了满足Python课程的一个作业要求，目的是学习如何实现基本的网络爬取和数据存储技术。

## 功能
- 抓取指定关键词的新闻数据。
- 将新闻数据存储到MySQL数据库中。
- 处理常见的网络错误和数据库错误，确保程序的稳定运行。

## 技术栈
- Python: 用于实现爬虫和数据库操作的主要编程语言。
- MySQL: 存储爬取的数据。
- Requests: 用于发送HTTP请求。
- Regular Expressions: 用于从HTML中解析数据。

## 安装
确保你的机器上已安装Python和MySQL。然后，你需要安装Python的依赖库：

```bash
pip install pymysql requests
```

## 使用方法

1. 克隆这个仓库到你的机器上。
2. 确保MySQL数据库运行，并根据实际情况修改`connect_db()`函数中的数据库连接参数。
3. 运行以下命令：

```
python news_scraper.py
```