"""
Text User interface for searching on discogs.
"""
import curses
from curses.textpad import Textbox, rectangle


def enter_is_terminate(x):
    """This thing makes enter terminate the input."""
    if x == 10:
        return 7
    else:
        return x


def compact(input, maxlen=70):
    """Creates a compact string from a dict."""
    output = ""
    for item in input.items():
        if (len(output.split("\n")[-1]) + len(item)) >= maxlen:
            output += "\n"
        output += "{} ".format(item)
    return output


class ResultBox:
    """A box that shows results."""
    border = 1
    data = ""

    def __init__(self, window, y, x, height=7, width=70):
        self.width = width
        self.height = height
        rectangle(window, y, x, y + self.height, x + self.width)
        self.x = x + 1
        self.y = y + 1
        self.window = window

    def write(self, data):
        """Stream writer for entering input?"""
        for row in data.split("\n"):
            self.window.addstr(self.y + self.border, self.x + self.border, row)
            self.y += 1
        self.data = data
        self.window.refresh()
        return True


class SearchBar:
    """A text input object."""
    l8n_search_label = "Search:"
    input_width = 50
    input_height = 1
    border = 1
    y = 0
    x = 0

    def __init__(self, window):
        """Draw searchbar. Return TextBox."""
        window.addstr(self.border, self.x, self.l8n_search_label)
        editwin = curses.newwin(1, self.input_width, 1, len(self.l8n_search_label) + 2)
        rectangle(window,
                  self.y,
                  len(self.l8n_search_label) + self.border,
                  self.border + self.input_height,
                  len(self.l8n_search_label) + self.border + self.input_width + self.border)
        self.box = Textbox(editwin)


class Browser:
    def __init__(self, window):
        """Create a basic empty element"""
        self.window = window
        self.results = []
        self.searchbox = SearchBar(window)
        window.refresh()

        self.result_x = 0
        self.result_y = self.searchbox.input_height + self.searchbox.border
        self.query = ""

    def add_result(self, item):
        """Append a result item to the screen."""
        rows = len(item.keys())
        result_box = ResultBox(self.window, self.result_y, self.result_x, rows)
        self.result_y = rows + 3
        result_box.write(compact(item))
        self.results.append(result_box)

    def wait_for_input(self):
        """Gather input and return it."""
        self.searchbox.box.edit(enter_is_terminate)
        self.query = self.searchbox.box.gather()
        return self.query

    def refresh(self):
        """Refresh the window."""
        self.window.refresh()
