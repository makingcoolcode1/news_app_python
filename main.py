
import requests

print("\n**Welcome to the news search tool**")
print("\nYou will require an API key from newsapi.org to access the app")

def verify_api_key(api_key):

    test_url = f"https://newsapi.org/v2/everything?q=baltimore&apiKey={api_key}"

    test_request = requests.get(test_url)

    return test_request.status_code == 200

def get_news(news_input):

    URL = f"https://newsapi.org/v2/everything?q={news_input}&apiKey={api_key}"

    json = requests.get(URL).json()

    title_0 = json["articles"][0]["title"]
    description_0 = json["articles"][0]["description"]
    link_0 = json["articles"][0]["url"]

    title_1 = json["articles"][1]["title"]
    description_1 = json["articles"][1]["description"]
    link_1 = json["articles"][1]["url"]

    title_2 = json["articles"][2]["title"]
    description_2 = json["articles"][2]["description"]
    link_2 = json["articles"][2]["url"]

    print("\nTitle: ", title_0)
    print("\n", description_0)
    print("\nRead More: ", link_0)
    print("\nTitle: ", title_1)
    print("\n", description_1)
    print("\nRead More: ", link_1)
    print("\nTitle: ", title_2)
    print("\n", description_2)
    print("\nRead More: ", link_2)



while True:
    api_key = input("\nPlease enter your API key: ")

    if api_key.lower() == "exit":
        print("Exiting News App....")
        break

    if verify_api_key(api_key):
        print("\nAPI KEY VALIDATED!")
        break
    else:
        print("\nERROR! Failed to validate API key. Please check your key")


while True:

    news_input = input("\nEnter a search query: ")

    if news_input.lower() == "exit":
        break
    
    try:
        get_news(news_input)
    except:
        print("\nNo News Articles Found, Please try another search")
