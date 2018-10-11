from prompt_toolkit import prompt, HTML
import requests
import json
import pprint
class Log_in:
    def __init__(self):
        self.prompt_info()
        self.log_in()


    def prompt_info(self):
        #self.account = prompt("Enter account: ")
        bottom_toolbar = HTML("Douban <b><style bg='#DE0000'>Password</style></b>")
        #self.password = prompt("Enter password: ", is_password = True, bottom_toolbar=bottom_toolbar)
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
            Log_in.access_token = "Bearer " + response["access_token"]
            Log_in.expire = response["expires_in"]
            self.username = response["douban_user_name"]
            print("Log in success!")
            print("Welcome!", self.username)

        except:
            print("Log in fail")

class Play_list:
    url = "https://api.douban.com/v2/fm/app_channels"

    def __init__(self):
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
        headers = {"Authorization": Log_in.access_token}
        self.channel = json.loads(requests.get(Play_list.url, params = data, headers = headers ).text)['groups']

    def group_select(self):
        for idx in range(len(self.channel)):
            if idx == 0:
                print("0. 我的私人")
            else:
                print("{}. {}".format(idx,self.channel[idx]['group_name']))
        self.select = int(prompt("Enter a group number."))
    def channel_select(self):
        channel = self.channel[self.select]['chls']
        for idx in range(len(channel)):
            print(channel[idx]['name'])



class Player:
    pass


if __name__ == '__main__':
    login = Log_in()
    play_list = Play_list()
    play_list.group_select()
    play_list.channel_select()
