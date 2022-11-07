# from loader import bot
# import handlers
# from utils.set_bot_commands import set_default_commands
#
# if __name__ == '__main__':
#     set_default_commands(bot)
#     bot.infinity_polling()

"""
Файл для запуска бота и создания БД, в случае её отсутствия
"""

import handlers
from database.models import DataBaseModel
from loader import bot, logger


if __name__ == '__main__':
    DataBaseModel._init_user_tables()
    bot.infinity_polling()
    logger.info('bot start working')

