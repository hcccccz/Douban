from prompt_toolkit import prompt as p
from pprint import pprint
import requests
import json
import time

class Log_in:
    def __init__(self):
        self.prompt_info()
        self.log_in()


    def prompt_info(self):
        self.account = p("Enter account: ")
        self.password = p("Enter password: ", is_password = True)
    def log_in(self):
        data = {"apikey": "02646d3fb69a52ff072d47bf23cef8fd",
                "client_id": "02646d3fb69a52ff072d47bf23cef8fd",
                "client_secret": "cde5d61429abcd7c",
                "udid": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "douban_udid": "b635779c65b816b13b330b68921c0f8edc049590",
                "device_id": "b88146214e19b8a8244c9bc0e2789da68955234d",
                "grant_type": "password",
                "redirect_uri": "http://www.douban.com/mobile/fm",
                "username": "qjx2921038@126.com",
                "password": "ricky3155",
                }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        try:
            response = json.loads(requests.post("https://www.douban.com/service/auth2/token", data = data, headers = headers).text)
            self.access_token = "Bearer " + response["access_token"]
            self.expire = response["expires_in"]
            self.username = response["douban_user_name"]
            print("Log in success!")
            print("Welcome!", self.username)

        except:
            print("Log in fail")

class Play_list:
    channel_url = "https://api.douban.com/v2/fm/app_channels"
    song_url = "https://api.douban.com/v2/fm/playlist"
    def __init__(self):
        self.log_in = Log_in()
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
        headers = {"Authorization": self.log_in.access_token}
        try:
            self.channel = json.loads(requests.get(Play_list.channel_url, params = data, headers = headers ).text)['groups']
        except:
            print("Fail to get channel")

    def group_select(self):
        choices = list()
        for idx in range(len(self.channel)):
            if idx == 0:
                choice = dict()
                choice['name'] = "我的私人"
                choice['value'] = self.channel[idx]['group_id']
                choices.append(choice)
            else:
                choice = dict()
                choice['name'] = self.channel[idx]['group_name']
                choice['value'] = self.channel[idx]['group_id']
                choices.append(choice)




    def channel_select(self):
        channels = self.channel[self.gselect['group']]['chls']
        while len(channels) == 0:
            print(channels)
            print("This group is empty")
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



class Player:
    pass


if __name__ == '__main__':

    play_list = Play_list()
    play_list.group_select()
    play_list.channel_select()
    play_list.song()
