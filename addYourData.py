#「Add your data」から自動デプロイしたWeb Appsに対して、APIリクエスト

import requests
import json

url = "url"#https://ADDYOURDATA_APP_NAME.azurewebsites.net/conversation

headers = {
    'Content-Type': 'application/json',
}

data = {
    "messages": [
        {"role": "user", "content": "hello"}
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data, ensure_ascii=False).encode('utf-8'))

# レスポンスの内容を表示
print(response.text)
