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