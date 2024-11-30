import wikipedia
import warnings

# Ignore BeautifulSoup warnings
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")


def get_user_input(prompt="Enter page title: "):
    """Getting user input"""
    return input(prompt)


def main():
    print("Welcome to the Wikipedia Search Tool!")
    # Getting user input for the first time
    title = get_user_input()
    while title:
        try:
            # Disable autosuggest to avoid the API suggesting other pages
            page = wikipedia.page(title, auto_suggest=False)
            print_page_details(page)
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(f"(BeautifulSoup warning) \n{e.options[:5]}...")  # Show the first 5 options and end with an apostrophe