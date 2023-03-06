import json
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests

def send(msg):
    headers = {'Content-Type': 'application/json', "Charset": "UTF-8"}
# 这里替换为复制的完整 webhook 地址
    prefix = 'https://oapi.dingtalk.com/robot/send?access_token=ca576b8ea7bfc45d6f79a1b07ae6ab6d86eb25303d54c69a217ced93453aa1df'
    timestamp = str(round(time.time() * 1000))
# 这里替换为自己复制过来的加签秘钥
    secret = 'SEC3aee440fd3a26b761273b992b6b9ebabcbaf87743cd592262da334c0a025b5a1'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    url = f'{prefix}&timestamp={timestamp}&sign={sign}'

# 钉钉消息格式，其中 msg 就是我们要发送的具体内容
    data = {
        "at": {
            "isAtAll": False
        },
        "text": {
            "content": msg
        },
        "msgtype": "text"
    }

    return requests.post(url=url, data=json.dumps(data), headers=headers).text


send("我就是我，颜色不一样的火")