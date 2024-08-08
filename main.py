
import requests

print("\n**Welcome to the news app!")
print("\nPlease visit https://newsapi.org/ to sign up for an API key before proceeding")

def validate_api_key(api_key):

    test_url = f"https://newsapi.org/v2/everything?q=NFL&apiKey={api_key}"

    test_request = requests.get(test_url)

    return test_request.status_code == 200

def get_news_data(news_search):

    URL = f"https://newsapi.org/v2/everything?q={news_search}&apiKey={api_key}"

    json = requests.get(URL).json()

    json_itle_1 = json["articles"][0]["title"]
    json_description_1 = json["articles"][0]["description"]
    json_url_1 = json["articles"][0]["url"]

    print("\nTitle: ", json_itle_1)
    print("\n", json_description_1)
    print("\nRead More: ", json_url_1)

while True:

    api_key = input("\nEnter your API key: ")

    if api_key.lower() == "exit":
        print("\nExiting Program.....")
        break

    if validate_api_key(api_key):
        print("\nAPI Key Validated!")
        break
    else:
        print("\nERROR! Failed to valid API Key. Please enter a valid API key. ")
        continue
    


while True:
    news_search = input("\nEnter a keyword to search: ")

    if news_search.lower() == "exit":
        break

    try:
        (get_news_data(news_search))
    except:
        print("\nERROR! No news articles found!")
