
import requests

print("\n**WELCOME TO THE NEWS APP**")
print("\nTo use this program, please sign up for a free API key at openewsapi.org")
print("Type 'exit' at anytime to close the program")


def validate_api_key(api_key):

    test_url = f"https://newsapi.org/v2/everything?q=baltimore&apiKey={api_key}"

    test_request = requests.get(test_url)

    return test_request.status_code == 200

def get_news(news_search):

    url = f"https://newsapi.org/v2/everything?q={news_search}&apiKey={api_key}"

    json = requests.get(url).json()

    title_0 = json["articles"][0]["title"]
    description_0 = json["articles"][0]["description"]

    title_1 = json["articles"][1]["title"]
    description_1 = json['articles'][1]["description"]

    print("Title:", title_0)
    print("\n", description_0)
    print("\nTitle",title_1)
    print("\n", description_1)


while True:

    api_key = input("\nPlease enter your API key: ")

    
    if api_key.lower() == "exit":
        print("Exiting Program....")
        break


    if (validate_api_key(api_key)):
        print("\nAPI KEY VALID.....Proceeding to News App!\n")
        break
    else:
        print("ERROR! Failed to validate API key. Please check your key input")


while True:

    news_search = input("\nPlease enter a city to search ")

    if news_search.lower() == "exit":
        break

    try:
        get_news(news_search)
    except:
        print("No News Articles Found, Please enter another search query.")


