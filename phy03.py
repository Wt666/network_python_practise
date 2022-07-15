import base64
import requests
import time
import json
import pandas as pd
import traceback
import sys
import urllib3
from PIL import Image
urllib3.disable_warnings()
HEADERS_PORTAL = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    "Content-Type": "application/json",
    'authority': 'smsportal.jegotrip.com:8087',  # prod
    # 'authority': 'tsmsportal.jegotrip.com:8087', # stg
    'Host': '18.167.119.109:8087',  # STG
    'authorization': 'Basic ZXlKaGJHY2lPaUpNJNk1UWTBPVGd6TURFeE55d2laWGh3SWpveE5qUTVPVEUyTlRFM2ZRLmV5SjFhV1FpT2pFeE5pd2lkSGx3WlNJNk1UQXdMQ0p6WTI5d1pTSTZleUp5YjJ4bElqb2lRMDFKUVdSdGFXNVRZMjl3WlNJc0luTnRjeUk2TVN3aWRtOXBjQ0k2TVgxOS41OFpGMS1nVnNOTVIzeDdpRU84QlpVY25IRklNdkRRbG1PYnE5LXJKOUlWZ0Z5alh1WXltdllqdTNGTFZlRXhTNmR5ZjcyLTRwYTFIdWlWQl9VS1dXZzo='
    # authorization是登录状态，具有时效性
}


# # token的生成规则，有没有API可以获取token？
# token = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY0OTgzODM1OCwiZXhwIjoxNjQ5OTI0NzU4fQ.eyJ1aWQiOjU5OCwidHlwZSI6MTAwLCJzY29wZSI6eyJyb2xlIjoiQWRtaW5TY29wZSIsInNtcyI6MSwidm9pcCI6Mn19.1N43gJg2PfJKRHYjGeOLN1s02Y29LzVUeymlKAh6yn01kFr5lWyWBKLetPRtfSZGIZrNLNotZmMWXxn2xrgJVw"
# # 如何将token编码为authorization？
# authorization = b'ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoZENJNk1UWTBPVGd6T0RNMU9Dd2laWGh3SWpveE5qUTVPVEkwTnpVNGZRLmV5SjFhV1FpT2pVNU9Dd2lkSGx3WlNJNk1UQXdMQ0p6WTI5d1pTSTZleUp5YjJ4bElqb2lRV1J0YVc1VFkyOXdaU0lzSW5OdGN5STZNU3dpZG05cGNDSTZNbjE5LjFONDNnSmcyUGZKS1JIWWpHZU9MTjFzMDJZMjlMelZVZXltbEtBaDZ5bjAxa0ZyNWxXeVdCS0xldFBSdGZTWkdJWnJOTE5vdFptTVdYeG4yeHJnSlZ3Og=='

def fetch_imgCode_and_get_value():
    # 获取验证码和半自动输入验证码
    url_imgCode = 'https://smsportal.jegotrip.com:8087/public/verificationCode/imgCode'
    html = requests.post(url_imgCode)
    html = html.json()
    image_buf_str = html['data']['image_buf_str']
    image_code = html['data']['image_code']

    # 保存base64编码的图片为图片文件
    with open('image_code.jpg', 'wb') as f:
        f.write(base64.b64decode(image_buf_str))
    # 打开显示图片
    Image.open('image_code.jpg').show()
    image_value = input('请输入验证码：')
    return image_code, image_value

def login_and_update_header():
    # 进行登录来获取token，并将token编码，更新Header的authorization
    image_code, image_value = fetch_imgCode_and_get_value()
    url_login = 'https://smsportal.jegotrip.com:8087/public/client/login'
    data_login = {"account": "DEMO_Tong",
                  "password": "9xpjkGcy",
                  "image_code": image_code,
                  "captcha": image_value,
                  "nickname": "DEMO_Tong", "client_type": 100}
    html = requests.post(url_login, data=json.dumps(data_login), headers=HEADERS_PORTAL)
    html = html.json()
    token = html['data']['token']
    HEADERS_PORTAL['authorization'] = f"Basic {base64.b64encode(f'{token}:'.encode()).decode()}"



def post_data(url, dict_data):
    try:
        data = json.dumps(dict_data)
        # print("\nreq:{}".format(data))
        for _ in range(15):
            rsp = requests.post(url, data, verify=False, headers=HEADERS_PORTAL)
            if rsp.status_code == 200:  # API请求正常
                if rsp.json()['error_code'] == 1002: # 'en-us': 'Login status failure'
                    login_and_update_header()
                else:
                    return True, rsp
        # API请求异常
        return False, rsp
    except Exception as e:
        print(f'try except info: {e.args}')
        traceback.print_exc()
        info = sys.exc_info()
        print(info)
        return False, str(info)

def order_query():
    url = 'https://smsportal.jegotrip.com:8087/sms/order/query'
    dict_data = {"page":1,"page_size":1,"tenement_id":None,"pay_type":None,"product_name":"","order_code":"","order_state":[1,2,3,4,5]}
    flag, rsp = post_data(url, dict_data)
    print(rsp.text)

if __name__ == '__main__':
    order_query()
    print('program done.')