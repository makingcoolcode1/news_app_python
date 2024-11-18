
import requests
import os

def validate_key(api_key):

    test_url = f"https://newsapi.org/v2/everything?q=baltimore&apiKey={api_key}"

    test_request = requests.get(test_url).status_code

    return test_request == 200

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    


def get_news_data(news_search, api_key):

    URL = f"https://newsapi.org/v2/everything?q={news_search}&apiKey={api_key}"

    json = requests.get(URL).json()

    title_0 = json["articles"][0]["title"]
    title_1 = json["articles"][1]["title"]
    title_2 = json["articles"][2]["title"]

    description_0 = json["articles"][0]["description"]
    description_1 = json["articles"][1]["description"]
    description_2 = json["articles"][2]["description"]

    url_link_0 = json["articles"][0]["url"]
    url_link_1 = json["articles"][1]["url"]
    url_link_2 = json["articles"][2]["url"]

    print("\n\n\nTitle: " + title_0)
    print("\n" + description_0)
    print("\nRead More: " + url_link_0)
    print("\n\n\nTitle: " + title_1)
    print("\n" + description_1)
    print("\nRead More: " + url_link_1)    
    print("\n\n\nTitle: " + title_2)
    print("\n" + description_2)
    print("\nRead More: " + url_link_2)


print("\n\nWelcome to the news app!")
print("\nTo access the app, you must sign up for a free API key from openewsapi.org.")

api_key_valid = True

while api_key_valid:
    if api_key_valid:

        api_key = input("\nPlease enter your API key: ")

        if api_key.lower() == 'exit':
            print("Exiting Program....")
            exit(0)

        if api_key == "":
            print("\nERROR! Entry cannot be blank")
            continue

        if validate_key(api_key):
            print("API Key Validated")
            api_key_valid = True
            break
        else:
            print("ERROR! API Key not valid")
            continue

while True:

    news_search = input("\nEnter a news query: ")

    if news_search.lower() == "exit":
        exit(0)

    if news_search.lower() == "clear":
        cs_choice = input("Are you sure you want to clear the screen (y/n)")
        if cs_choice.lower() == "y":
            clear_screen()
        if cs_choice == "n":
            print("Screen will not clear")
        
        else:
            print("Invalid choice")

    if news_search not in ["clear", "exit"]:

        try:
            get_news_data(news_search, api_key)
        
        except:
            print("\nERROR! No news articles found!")