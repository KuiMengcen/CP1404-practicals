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
        except wikipedia.exceptions.PageError:
            print(f"\nPage id \"{title}\" does not match any pages. Try another id!")
        except Exception as e:
            print(f"An error occurred: {e}")

            # Getting new user input
        title = get_user_input("\nEnter page title: ")

    print("Thank you.")


def print_page_details(page):
    """Print page titles, summaries, and URLs."""
    print(f"\n{page.title}")
    print(wikipedia.summary(page.title, sentences=2))
    print(page.url)


if __name__ == "__main__":
    main()