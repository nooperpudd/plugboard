# encoding:utf-8

from plugboard.command import BaseCommand


class Command(BaseCommand):
    """
    """
    name = "app"
    description = "create app engine"

    def add_arguments(self, parser):

        pass
         # parser.add_argument("", dest="", required=True, help="create project name")

    def handler(self, *args, **options):
        name = options.get("name")


    def notify(self, *args, **kwargs):
        pass
