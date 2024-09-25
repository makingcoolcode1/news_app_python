
import requests

print("\n**WELCOME TO THE NEWS APP**")
print("\nTo get started, you will need an API key from newsapi.org")

def api_validation():

    test_url = f"https://newsapi.org/v2/everything?q=baltimore&apiKey={api_key}"

    test_result = requests.get(test_url)

    return test_result.status_code == 200

def search_news(news_search):
    URL = f"https://newsapi.org/v2/everything?q={news_search}&apiKey={api_key}"

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


exit_program = False


while True:

    api_key = input("\nPlease Enter your API Key: ")

    if api_key.lower() == "exit":
        print("\nExiting Program....")
        exit_program = True
        break
    


    if api_validation():
        print("\nAPI Key Validated!")
        break
    else:
        print("\nERROR: Failed to validated API key. Please try another key")
    



if not exit_program:
    while not exit_program:

        news_search = input("\nPlease enter a search query ")

        if news_search.lower() == "exit":
            print("\nExiting Program....")
            exit_program == True
            break
    
        
        try:
            search_news(news_search)
        except:
            print("ERROR: No news particles found")


