import requests

while 0 == 0:
    print("JJREQUEST")
    url = str(input("enter URL of site you want the source code for: "))
    # Be sure to include www and the protocol the site uses.
    
    x = requests.get(url)
    print(x.text)

    yn = str(input("again? (y/n): "))
    if yn == str("n"):
        quit()
    else:
        continue
