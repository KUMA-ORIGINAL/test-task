from django.core.management.base import BaseCommand

from bot.views_bot import tbot

log = logger.bind(task="app")


class Command(BaseCommand):
    """Команда для запуска бота в режиме long polling."""

    help = 'command for start bot long polling mode'

    def handle(self, *args, **options):
        """Entrypoint."""
        log.info('Start long polling...')
        tbot.infinity_polling()