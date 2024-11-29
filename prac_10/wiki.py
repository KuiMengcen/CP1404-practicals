import wikipedia
import warnings

#Ignore BeautifulSoup warnings
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")

def get_user_input(prompt="Enter page title: "):
    """Get user input"""
    return input(prompt)