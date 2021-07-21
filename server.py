import vk_api.vk_api
from control_pc import *

from config import my_vk_id

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        self.server_name = server_name

        self.vk = vk_api.VkApi(token=api_token)

        self.long_poll = VkBotLongPoll(self.vk, group_id)

        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, message, attachment=None):
        if attachment:
            self.vk_api.messages.send(peer_id=send_id,
                                      message=message,
                                      attachment=attachment,
                                      random_id=0)
        else:
            self.vk_api.messages.send(peer_id=send_id,
                                      message=message,
                                      random_id=0)

    def test(self):
        self.send_msg(my_vk_id, "Привет-привет!")

    def send_image(self, user_id, image, text):
        upload = vk_api.VkUpload(self.vk)
        photo = upload.photo_messages(image)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        self.send_msg(user_id, text, attachment=attachment)

    def control_vk(self, dictionary, user_id):
        if dictionary:
            if dictionary['type'] == 'screenshot' or dictionary['type'] == 'web_camera':
                self.send_image(user_id, dictionary['attachment'], dictionary['text'])

    def start(self):
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                user_id = event.message['from_id']
                if user_id == my_vk_id:
                    text = ''
                    if event.message['text']:
                        text = event.message['text']

                    elif event.message['attachments']:
                        attach = event.message['attachments'][0]
                        if attach['type'] == 'audio_message':
                            print(attach)
                            self.send_msg(user_id, 'Голосовое сообщение')

                    dictionary = control_pc(text)
                    self.control_vk(dictionary, user_id)
