#　push成功。どうやらGitHubと接続されていることを確認
# ライブラリが不足していたので、conda acitvateしてから、anaconda-navigatorで追加。
#　conda環境で、一応ある程度は動いている。


import json
import urllib.request
import pprint
import pandas as pd

api_key = {'X-API-KEY':'LN77WqibkBF95xnAQRtUFzbqtvDkwpf3LcG2exKq'}
url = 'https://opendata.resas-portal.go.jp/api/v1/prefectures'

req = urllib.request.Request(url, headers=api_key)

with urllib.request.urlopen(req) as response:
    data = response.read()

d = json.loads(data.decode())

#整形して出力
pprint.pprint(d)





#{'description': '', 'message': 'Forbidden.', 'statusCode': '403'}
#どうやら、RESASでAPIキーが確認できない場合に返すエラー
#アクセス成功！