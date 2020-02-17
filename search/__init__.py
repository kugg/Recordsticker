"""
A discogs_client based search query utility with filtering support.
"""
import configparser

import discogs_client


class Conf(configparser.ConfigParser):
    """A class to store configuration items."""

    def __init__(self, filename):
        super(Conf, self).__init__()
        self.filename = filename
        self.read(self.filename)

    def _write(self):
        with open(self.filename, 'w') as configfile:
            self.write(configfile)

    def save(self):
        """Write current config to file and read it again."""
        self._write(self)
        self.read(self.filename)


def query(catalog_number):
    """Implement a top level search query for catalog number."""
    api_conf = Conf("search/api.ini")
    connection = discogs_client.Client(api_conf['client']['user_agent'],
                                        user_token=api_conf['user']['user_token'])
    results = connection.search(catalog_number, type='catno')
    return results


def result_filter(search_result):
    """Filter key values from a configured list of search results."""
    filter_conf = Conf("search/filter.ini")
    dict_filter = filter_conf["filter"]
    filter_true = filter(dict_filter.getboolean, dict_filter)
    shown_result = {}
    try:
        for key in filter_true:
            shown_result[key] = search_result[key]
    except KeyError as e:
        print("The result from the query did not have field requested in filter config. {}".format(e))
    return shown_result


def test():
    """Top level test for this package."""
    results = query("W-90629")
    result = results[0]
    dict_result = vars(result)['data']
    shown = result_filter(dict_result)
    print(shown)
