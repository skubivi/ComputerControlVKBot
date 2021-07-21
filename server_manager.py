from server import Server

from config import *

server1 = Server(vk_api_token, vk_group_id, 'server1')

server1.start()
