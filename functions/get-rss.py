import feedparser
import helpers


@helpers.time_count
def get_rss_records(url):
    print("get_rss_records - starting")
    news_feed = feedparser.parse(url)
    return news_feed


def handler(event, context):
    print(event)
    url = event['site']
    print(url)
    try:
        func_res_dict = get_rss_records(url)
        print('after get_rss_records')
        # print(func_res_dict)
        items = func_res_dict['func_result'].entries[:5]
        # print(items)
        result = []
        for item in items:
            print(item)
            print(item.title)
            print(item.link)
            result.append({"title": item.title, "link": item.link})

        print(result)
        return {"url": url, "content": result, "time": func_res_dict['period']}

    except Exception as err:
        print(f'Error occurred: {err}')
