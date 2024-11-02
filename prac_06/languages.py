from programming_language import ProgrammingLanguage

def main():

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    dynamic_language = [languages.name for language in languages if language.is_dynamic()]

    for language in languages:
            print(language.name)