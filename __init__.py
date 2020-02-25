"""A Discogs record search client that can generate printing labels."""
import search
import ui.terminalui

def main():
    """
    Take a search term using a suitable UI driver and let the user choose a label to print.
    """
    while True:
        browser = ui.terminalui.curses.wrapper(ui.terminalui.Browser)
        query = browser.wait_for_input()
        results = search.search(query)
        # results = [{'style': ['Bop'], 'title': 'The Oscar Peterson Trio - Night Train', 'country': 'US', 'community': {'want': 77, 'have': 61}, 'label': ['Verve Records', 'Capitol Records, Inc.', 'Verve Records'], 'catno': 'V-8538', 'year': '1963', 'genre': ['Jazz'], 'type': 'release'}, {'style': ['Bop'], 'title': 'The Oscar Peterson Trio - Night Train', 'country': 'US', 'community': {'want': 45, 'have': 76}, 'label': ['Verve Records', 'Capitol Records, Inc.'], 'catno': 'V6-8538', 'year': '1963', 'genre': ['Jazz'], 'type': 'release'}]

        for result in results:
            browser.add_result(result)
            browser.wait_for_input()


if __name__ == "__main__":
        main()
