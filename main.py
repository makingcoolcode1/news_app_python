
import requests

print("\n**Welcome to the news app**")
print("\nYou will need an API key from https://newsapi.org..... Please use the link to sign up for a free key")


def validate_key(api_key):

    test_url = f"https://newsapi.org/v2/everything?q=NFL&apiKey={api_key}"

    test_key = requests.get(test_url)

    return test_key.status_code == 200

def search_news(news_search):

    URL = f"https://newsapi.org/v2/everything?q={news_search}&apiKey={api_key}"

    json = requests.get(URL).json()

    title_pull_0 = json["articles"][0]["title"]
    description_pull_0 = json["articles"][0]["description"]

    title_pull_1 = json["articles"][1]["title"]
    description_pull_1 = json["articles"][1]["title"]

    print(f"\nTitle: ", title_pull_0)
    print(f"\nDescription: ", description_pull_0)
    print("\nTitle:", title_pull_1)
    print("\nDescription: ", description_pull_1)

while True:

    api_key = input("\nEnter your API key: ")

    if api_key.lower() == "exit":
        print("Exiting Program....")
        break

    if (validate_key(api_key)):
        print("API Key Validated!")
        break
    else:
        print("ERROR! Failed to validate API key..")


while True:

    news_search = input("Enter a keyword: ")

    try:

        (search_news(news_search))
    
    except:
        print("\nERROR: No news articles found.....")

    if news_search.lower() == "exit":
        print("Exiting Program")
        break