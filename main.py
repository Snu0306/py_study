from requests import get

websites = (
    "https://google.com",
    "airbnb.com",
    "twitter.com",
    "https://facebook.com",
    "ticktok.com"
)
for website in websites :
    if not website.startswith("https://"):
        website = f"https://{website}"     
    response = get(website)
    print(response)
    