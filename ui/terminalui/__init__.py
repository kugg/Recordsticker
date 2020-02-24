"""
Text User interface for searching on discogs.
"""
import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper


class ResultBox:
    """A box that shows results."""
    width = 70
    height = 5
    border = 1

    def __init__(self, window, result_text, x, y):
        rectangle(window, y, x, y + self.height, x + self.width)
        self.x = x
        self.y = y
        window.addstr(self.y + self.border, self.x + self.border, result_text)
        # TODO: Write a result box  that can take a result dict and rpesent it efficiently as a label


def enter_is_terminate(x):
    """This thing makes enter terminate the input."""
    # TODO: Handle backspace as erase left (Ctrl + h)
    if x == 10:
        return 7
    else:
        return x


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


def main(fullscreen):
    """Main functino to draw things"""
    searchbox = SearchBar(fullscreen)
    fullscreen.refresh()
    searchbox.box.edit(enter_is_terminate)
    message = searchbox.box.gather()

    # TODO: Draw results here.
    fullscreen.addstr(4, 0, message)
    fullscreen.refresh()
    searchbox.box.edit(enter_is_terminate)
    # TODO: Organize results boxes with search results.
    return 0


wrapper(main)

