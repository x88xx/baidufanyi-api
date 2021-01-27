import random
import hashlib
import json
import requests

appid: str = ''
key: str = ''


# http://api.fanyi.baidu.com/api/trans/product/apichoose

class Translation:
    _url: str = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    # url: str  = 'http://fanyi-api.baidu.com/api/trans/vip/translate'
    _data: dict = {
        'q': '',
        'from': '',
        'to': '',
        'salt': '',
        'sign': ''
    }
    _headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    def __init__(self, query, from_data, to, appid, key):
        self._data['q'] = query
        self._data['from'] = from_data
        self._data['to'] = to
        self._data['appid'] = appid
        self._data['salt'] = str(random.randint(0000000000, 9999999999))
        self._data['sign'] = hashlib.md5((appid + self._data['q'] +
                                          self._data['salt'] +
                                          key).encode(encoding='UTF-8')).hexdigest()

    def post(self) -> str:
        data = requests.post(url=self._url, data=self._data, headers=self._headers).text
        return data


def run(text, from_data, to):
    data = json.loads(Translation(text, from_data, to, appid, key).post())
    print(data['trans_result'][0])


if __name__ == '__main__':
    run('人生苦短，我学Python', 'zh', 'en')
