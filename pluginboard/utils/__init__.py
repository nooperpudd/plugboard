# encoding:utf-8


def check_dict_common_keys(dict_list):
    """
    check the dict common keys in the dict list
    :param dict_list: [{},{}...]
    :return: set()
    """
    if len(dict_list) >= 2:
        common_keys = set(dict_list[0].keys())
        for dict_item in dict_list[1:]:
            common_keys.intersection_update(set(dict_item.keys()))
        return common_keys
