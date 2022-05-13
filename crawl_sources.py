import requests

hd = {'user-agent': 'Mozilla/5.0'}
url = "http://m.wufazhuce.com/article/999"
path = "./article.htm"

if __name__ == '__main__':
    try:
        r = requests.get(url, headers=hd)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        with open(path, 'w', encoding="utf-8") as f:
            f.write(r.text)
        print("OK")
    except Exception as e:
        print(e)
