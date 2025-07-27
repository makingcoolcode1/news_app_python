
import os
import requests


def clear_consol():
    if os.name == "nt":
        os.system("cls")

def validate_key(api_key):

    url = f"https://newsapi.org/v2/everything?q=baltimore&apiKey={api_key}"

    test_request = requests.get(url).status_code

    return test_request == 200

api_key_validation = False

while api_key_validation == False:
    
    api_key = input("Please enter your API key: ")

    if api_key.lower() == "exit":
        exit_choice = input("Are you sure you want to exit the News App? y/n: ")

        if exit_choice.lower() == "y":
            exit(0)
        elif exit_choice.lower() == 'n':
            print("Exit Aborted")
        else:
            print("ERROR: Invalid Choice")
        continue
    
    if api_key.lower() == "clear":
        
        clear_choice = input("Do you want to clear the screen?: y/n")

        if clear_choice == 'y':
            clear_consol()
        elif clear_choice == "n":
            print("Screen Clear Aborted!")
        else:
            print("ERROR! Invalid Choice")
        continue
    

    if validate_key(api_key):
        print("API KEY VALID")
        import news_ui as news_ui
        api_key_validation = True
    else:
        print("ERROR! Could not validate API key")


