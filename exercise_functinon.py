
def myLanguages():

    languages = ["English", "Spanish", "French", "German"]

    for language in languages :
        result = input("Can you speak " + language + "?" + " (yes/no) " + "\n")
        if language == "English":
            print("I can speak English.")
        elif language == "Spanish":
            print("I can speak Spanish.")
        else:
            print("I cannot speak this language.")

myLanguages()