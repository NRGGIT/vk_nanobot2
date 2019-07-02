import vk_api
import random
from config import *

vkBot = vk_api.VkApi(token = BOT_TOKEN)

USER_ID = 2299551 #здесь пишите свой id
text = 'Это сообщение отправленно с помощью vk_api 222222'
result = vkBot.method('messages.send', {'user_id' : USER_ID,
                                        'random_id' : random.randint(1, 2147483648),
                                        'message' : text})
print(result)