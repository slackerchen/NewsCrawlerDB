import requests
import re
import time
import pymysql


def connect_db():
    return pymysql.connect(host='localhost', user='root', password='123456', database='hot_topics')


def create_table(cur):
    cur.execute('''
        CREATE TABLE IF NOT EXISTS hot_topics (
            keyword VARCHAR(20),
            title VARCHAR(100),
            url VARCHAR(200),
            source VARCHAR(20),
            date VARCHAR(20)
        )
    ''')


def insert_data(cur, data):
    sql = 'INSERT INTO hot_topics (keyword, title, url, source, date) VALUES (%s, %s, %s, %s, %s)'
    cur.execute(sql, data)


def fetch_news(keyword, page):
    url = f'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd={keyword}&pn={page * 10}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raises HTTPError, if one occurred

    return response.text


def parse_html(html):
    titles = re.findall('<h3 class="news-title_1YtI1 ">.*?>(.*?)</a>', html, re.S)
    urls = re.findall('<h3 class="news-title_1YtI1 "><a href="(.*?)"', html, re.S)
    dates = re.findall('<span class="c-color-gray2 c-font-normal c-gap-right-xsmall".*?>(.*?)</span>', html)
    sources = re.findall('<span class="c-color-gray" .*?>(.*?)</span>', html)

    return titles, urls, dates, sources


def main(keywords):
    conn = connect_db()
    cur = conn.cursor()
    create_table(cur)
    conn.commit()

    for keyword in keywords:
        for page in range(1, 6):  # Fetch the first 5 pages
            try:
                html = fetch_news(keyword, page)
                titles, urls, dates, sources = parse_html(html)
                for title, url, date, source in zip(titles, urls, dates, sources):
                    data = (keyword, title.strip(), url, source, date)
                    insert_data(cur, data)
                conn.commit()
                print(f'Successfully fetched page {page} for {keyword}')
            except Exception as e:
                print(f'Failed to fetch page {page} for {keyword}: {e}')
            time.sleep(5)

    cur.close()
    conn.close()


if __name__ == '__main__':
    main(['人机交互', '大数据', '机器学习', '气候变迁', '智能驾驶'])  # Example keywords
