class Local(object):
    """
    """
    DEBUG = False

    COMMANDS = ["tests.user_commands.default_command",
                "tests.user_commands.cac_command"]


class Product(Local):
    COMMANDS = ["sample.nono",
                "sample.haha"]
