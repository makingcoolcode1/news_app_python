
import requests
import os

def validateKey(api_key):

    testURL = f"https://newsapi.org/v2/everything?q=baltimore&apiKey={api_key}"

    test_request = requests.get(testURL).status_code

    return test_request == 200

def get_news_data(news_search, api_key):
   
   URL =  f"https://newsapi.org/v2/everything?q={news_search}&apiKey={api_key}"

   json = requests.get(URL).json()

   title_0 = json["articles"][0]["title"]
   title_1 = json["articles"][1]["title"]
   title_2 = json["articles"][2]["title"]
   
   description_0 = json["articles"][0]["description"]
   description_1 = json["articles"][1]["description"]
   description_2 = json["articles"][2]["description"]


   print("\nTitle: ", title_0)
   print("\n", description_0)
   
   print("\nTitle: ", title_1)
   print("\n", description_1)

   print("\nTitle", title_2)
   print("\n", description_2)

def clear_screen():
    if os.name == "nt":
        os.system("cls")

print("\Welcome to the news app!")
print("\nTo continue, you will need to have an API key from opennewsapi.com")

apiKeyValid = True

while apiKeyValid:
    if apiKeyValid:

        api_key = input("\nEnter your API Key: ")
        
        if validateKey(api_key):
            print("\nAPI KEY VALID")
            break
        else:
            print("ERROR! API KEY NOT VALID")


        if api_key.lower() == "exit":
            print("\nExiting Program....")
            apiKeyValid = False
            exit()


while True:
    
    news_search = input("\nPlease enter a search query: ")
        
    if news_search.lower() == "clear":
        confirm = input("\nAre you sure you wan to clearn the screen? (y/n)")
        
        if confirm == "y":
            clear_screen()
            
        else:
            print("Screen Clear Canceled")
            continue


    elif news_search.lower() == "exit":
        print("\nExiting Program....")
        exit()

    if news_search not in ["clear", "exit"]: 
        try:
            get_news_data(news_search, api_key)
        
        except:
            print("\nERROR! No news articles found. Please try another entry.")

        



    

