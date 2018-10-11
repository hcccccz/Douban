from prompt_toolkit import prompt, HTML
import requests
import json
class Log_in:
    def __init__(self):
        self.prompt_info()
        self.log_in()


    def prompt_info(self):
        self.account = prompt("Enter account: ")
        bottom_toolbar = HTML("Douban <b><style bg='#DE0000'>Password</style></b>")
        self.password = prompt("Enter password: ", is_password = True, bottom_toolbar=bottom_toolbar)
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
        try:
            response = json.loads(requests.post("https://www.douban.com/service/auth2/token", data = data, headers = headers).text)
            self.access_token = "Bearer" + response["access_token"]
            self.expire = response["expires_in"]
            self.username = response["douban_user_name"]
            print("Log in success!")

        except:
            print("Log in fail")

#class Player:
    #def __init__(self):

if __name__ == '__main__':
    login = Log_in()
