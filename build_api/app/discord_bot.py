import requests


class DiscordBot():
    def __init__(self):
        self.url = "https://discord.com/api/webhooks/1379312413987569714/5ZPASJcN_gWSV692D5BuTvvWnZGZi0EJkDYz91yl4DtrXRnSqoAx8ZXvJ_lrMHX3cqzW"
        self.headers = {"Authorization": ""}
    
    def send_message(self, text):
        payload = {"content": text}
        requests.post(self.url, payload, headers=self.headers)

if __name__ == '__main__':
    bot = DiscordBot()
    bot.send_message('Send from python \n@everyone')