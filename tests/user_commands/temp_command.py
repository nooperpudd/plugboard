# encoding:utf-8

# encoding:utf-8
from plugboard.command import BaseCommand


class Command(BaseCommand):

    name = "app"
    description = "help user to create the app with the branch and with env."

    def add_arguments(self, parser):
        pass

    def handler(self, *args, **options):
        pass

    def notify(self, *args, **kwargs):
        pass
