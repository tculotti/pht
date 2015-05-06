"""
Keywords to manipulated strings
"""

def convert_to_upper_case(value):
    """
    Coverts a string to UPPERCASE
    :param value:
    :return:
    """
    string = value.upper()
    return string


def convert_to_lower_case(value):
    """
    Converts a sting to lower case
    :param value:
    :return:
    """
    string = value.lower()
    return string


def convert_to_title_case(value):
    """
    Converts a string to Title Case
    :param value:
    :return:
    """
    string = value.title()
    return string


def split_string_to_list(the_string, the_delimeter):
    """
    splits a string into a list based on a delimter
    :param the_string:
    :param the_delimeter:
    :return:
    """
    return the_string.split(the_delimeter)

def sort_unicode_list_lower(the_list):
    """
    sorts a string by alphabetical lower case
    example
    sort_unicode_list_lower(A, b, a , B, C, s) will return
    a, A, b, B, C, s
    :param the_list:
    :return:
    """
    return sorted(the_list, key=unicode.lower)

def convert_list_to_tuple(list):
    return  tuple(list)
