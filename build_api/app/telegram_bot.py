from io import BytesIO

import cv2
import requests


class TelegramBot():
    def __init__(self):
        self.id = '1755265309'
        
        token = '7620474246:AAEbtJBFtK7AdEFaTVuQTJsOyt2vc3SCHsc'
        self.message_url = f'https://api.telegram.org/bot{token}/sendMessage'
        self.photo_url = f'https://api.telegram.org/bot{token}/sendPhoto'
    
    def send_message(self, message):
        data = {'chat_id':id, 'text': message}
        requests.post(self.message_url, data=data)

    def send_photo(self, image, caption=''):
        _, buffer = cv2.imencode('.png', image)
        file = BytesIO(buffer.tobytes())
        file.name = 'image.png'

        files = {'photo': file}
        data = {'chat_id': self.id, 'caption': caption}
        requests.post(self.photo_url, data=data, files=files)

if __name__ == '__main__':
    bot = TelegramBot()
    image = cv2.imread('../test.jpg')
    bot.send_photo(image, 'test')