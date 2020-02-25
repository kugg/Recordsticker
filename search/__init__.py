"""
A discogs_client based search query utility with filtering support.
"""
import configparser

import discogs_client


class Conf(configparser.ConfigParser):
    """A class to read and store configuration items."""

    def __init__(self, filename):
        super(Conf, self).__init__()
        self.filename = filename
        self.read(self.filename)

    def _write(self):
        with open(self.filename, 'w') as configfile:
            self.write(configfile)

    def save(self):
        """Write current config to file and read it again."""
        self._write()
        self.read(self.filename)

    def enabled(self, section):
        """Return all enabled config keys for a given section"""
        enabled = []
        for item in self[section].keys():
            if self[section].getboolean(item):
                enabled.append(item)
        return enabled

def query(catalog_number):
    """
    Search query for catalog number.
    Return a list of discogs_client.Results.
    """
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
        pass
        # print("The result from the query did not have field requested in filter config. {}".format(e))
    return shown_result


def search(catalog_number):
    """
    A top level `catalog_number` search that returns a list of result dicts.
    Usually catalog numbers are unique but not always hence the returned list.
    """
    results = query(catalog_number)
    result_list = []
    for result in results:
        dict_result = vars(result)["data"]
        result_list.append(result_filter(dict_result))
    return result_list


def test_search():
    """Top level test for this package."""
    search("W-90629")
    return True


def test_config():
    """Test to see if config can read and write."""
    filter_conf = Conf("search/filter.ini")
    item = "Test"
    filter_conf[item] = {}  # Create section
    filter_conf[item][item] = item  # Create option
    filter_conf.save()
    if filter_conf[item][item] == item:
        filter_conf.remove_option(item, item)
        filter_conf.remove_section(item)
        filter_conf.save()
        if not filter_conf.has_option(item, item):
            return True
    return False
