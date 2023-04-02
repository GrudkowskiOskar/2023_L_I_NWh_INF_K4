
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, Oskar, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, Oskar)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, Oskar)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, Oskar)
    elif format == JSON:
        result = format_to_json(msg, Oskar)
    return result


def format_to_json(msg, Oskar):
    return ('{ "imie":"' + Oskar + '", "mgs":' +
            msg + '"}')


def plain_text(msg, Oskar):
    return imie + ' ' + msg


def plain_text_upper_case(msg, Oskar):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, Oskar):
    return plain_text(msg.lower(), imie.lower())
