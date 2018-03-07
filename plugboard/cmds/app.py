# encoding:utf-8

from plugboard.command import BaseCommand


class Command(BaseCommand):
    """
    """
    name = "app"
    description = "create app engine"

    def add_arguments(self, parser):
        pass

    def handler(self, *args, **options):
        pass

    def notify(self, *args, **kwargs):
        pass
