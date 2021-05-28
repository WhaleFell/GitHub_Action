import requests
import logging
logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='new.log',
                    filemode='w',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )
logging.StreamHandler()

class CoolPush(object):

    def __init__(self, token):
        self.token = token
        self.headers = {
            "User-Agent": "Mozilla/5.0 (WeiboMonitor; Win64; x64) Chrome/80.0.3987.163 Safari/537.36"
        }

    def pushSend(self, content):
        url = "https://push.xuthus.cc/send/%s" % (self.token)
        data = {
            "c": content,
        }
        try:
            resp = requests.get(url, headers=self.headers, params=data)

            if resp.json()["code"] != 200:
                logging.warning("[CoolPush]推送出现异常,响应:%s" % (resp.text))
            else:
                logging.info("[CoolPush]推送成功")
        except:
            logging.warning("[CoolPush]推送失败!")

    def pushGoup(self, content):

        url = "https://push.xuthus.cc/group/%s" % (self.token)
        data = {
            "c": content,
        }
        try:
            resp = requests.get(url, headers=self.headers, params=data)

            if resp.json()["code"] != 200:
                logging.warning("[CoolPush]推送出现异常,响应:%s" % (resp.text))
            else:
                logging.info("[CoolPush]推送成功")
        except:
            logging.warning("[CoolPush]推送失败!")


if __name__ == "__main__":
    token = "92f83d0596c7b553ea1df9f242e4fc46"
    bot = CoolPush(token)
    bot.pushSend("GitHub Action")
