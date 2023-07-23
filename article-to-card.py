import requests

# Replace YOUR_API_KEY with your actual API key
url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=398c1f3ab1ed4fba8f15d3173d88b0bd"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    articles = data["articles"]
    for article in articles:
        title = article["title"]
        description = article["description"]
        content = article["content"]
        if content:
            summary = content.split(". ")[0:5]
            summary = ". ".join(summary) + "."
        else:
            summary = description
        print(title)
        print(summary)
        print()
else:
    print("Error:", response.status_code)
