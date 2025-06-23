import requests


class DiscordBot():
    def __init__(self):
        self.url = ""
        self.headers = {"Authorization": ""}
    
    def send_message(self, text):
        payload = {"content": text}
        requests.post(self.url, payload, headers=self.headers)

if __name__ == '__main__':
    bot = DiscordBot()
    bot.send_message('Send from python \n@everyone')
