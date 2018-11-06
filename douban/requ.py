from pprint import pprint
import requests
import json
import time

class Log_in:
    def __init__(self):
        self.account = "" #登录
        self.password = "" #登录
        self.info = {} #返回


    def log_in(self):
        data = {"apikey": "02646d3fb69a52ff072d47bf23cef8fd",
                "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
                "client_secret": "cde5d61429abcd7c",
                "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
                "device_id": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "grant_type": "password",
                "redirect_uri": "http://www.douban.com/mobile/fm",
                "username": self.account,
                "password": self.password,
                }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = json.loads(requests.post("https://www.douban.com/service/auth2/token", data = data, headers = headers).text)
        print(response)

        self.info["username"] = response["douban_user_name"]
        self.info["access_token"] = "Bearer " + response["access_token"]
        self.info["expire"] = response["expires_in"]


    def set_info(self,account,password):
        self.account = account
        self.password = password

    def ret_info(self):
        return self.info





class Group_list:
    channel_url = "https://api.douban.com/v2/fm/app_channels"
    song_url = "https://api.douban.com/v2/fm/playlist"
    def __init__(self):
        self.username = ""
        self.expire = ""
        self.access_token = ""

    def set_info(self,info:dict):
        self.username = info['username']
        self.expire = info['expire']
        self.access_token = info['access_token']


    def request(self):
        data = {"alt": "json",
                "app_name": "radio_iphone",
                "apikey": "02646d3fb69a52ff072d47bf23cef8fd",
                "client": "s:mobile|y:iOS 10.2|f:115|d:b88146214e19b8a8244c9bc0e2789da68955234d|e:iPhone7,1|m:appstore",
                "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
                "icon_cate": "xlarge",
                "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
                "version": 115,
                }
        headers = {"Authorization": self.access_token}
        return json.loads(requests.get(Group_list.channel_url, params = data, headers = headers ).text)['groups']

    def group(self,response):

        choices = list()
        for idx in range(len(response)):
            if idx == 0:
                choice = dict()
                choice['name'] = "我的私人"
                choice['value'] = response[idx]['group_id']
                choices.append(choice)
            else:
                choice = dict()
                choice['name'] = response[idx]['group_name']
                choice['value'] = response[idx]['group_id']
                choices.append(choice)
        return choices



"""
    def channel_select(self):
        channels = self.channel[self.gselect['group']]['chls']
        while len(channels) == 0:
            print(channels)
            print("This group is empty?")
            time.sleep(0.5)
            self.group_select()
            channels = self.channel[self.gselect['group']]['chls']
        choices = list()
        for idx in range(len(channels)):
            choice = dict()
            choice['name'] = channels[idx]['name']
            choice['value'] = channels[idx]['id']
            choices.append(choice)




    def song(self):
        headers = {"Authorization":self.log_in.access_token}
        data = {
            "channel": self.cselect['channel'],
            "from": "mainsite",
            "pt": "0.0",
            "kbps": "128",
            "formats": "aac",
            "alt": "json",
            "app_name": "radio_iphone",
            "apikey": "02646d3fb69a52ff072d47bf23cef8fd",
            "client": "s:mobile|y:iOS 10.2|f:115|d:b88146214e19b8a8244c9bc0e2789da68955234d|e:iPhone7,1|m:appstore",
            "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
            "icon_cate": "xlarge",
            "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
            "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
            "version": "115",
            "type": "n"
        }
        response = requests.get(self.song_url,headers=headers,params=data)
        print(response.status_code)

"""

class Player:
    pass


if __name__ == '__main__':
    login = Log_in()
    login.set_info("qjx2921038@126.com","ricky3155")
    login.log_in()
    print(type(login.ret_info()))
    group_list = Group_list(login.ret_info())
    reponse = group_list.request()
    print(group_list.group(reponse))
