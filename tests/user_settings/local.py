class Local(object):
    """
    """
    DEBUG = False

    COMMANDS = ["sample.hello"]


class Product(Local):
    COMMANDS = ["sample.nono",
                "sample.haha"]
