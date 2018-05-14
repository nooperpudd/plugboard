# encoding:utf-8

from pluginboard.command import BaseCommand


class Command(BaseCommand):
    name = "test"
    description = "help user to create the app with the branch and with env."

    def add_arguments(self, parser):
        sub_parsers = parser.add_subparsers(help="list sub command names")

        test_parser = sub_parsers.add_parser("hello", help="say hello",
                                             add_help=True)
        test_parser.add_argument("--name", dest="name", type=str,
                                 help="hello name")
        #
        # create_parser.add_argument('-h', '--help', action=HelpAction, channel_id=self.channel_id,
        #                            default=argparse.SUPPRESS, help='show this help message')
        test_parser.set_defaults(func=self.test_parser)

    def test_parser(self, **kwargs):
        name = kwargs.get("name")
        print(name)
