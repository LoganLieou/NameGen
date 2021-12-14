import random
import os
import requests
from bs4 import BeautifulSoup


def main():
    # read in contents of list file which contains a list of all foods
    if ("list.txt" in os.listdir(".")):
        with open("list.txt", "r") as f:
            lines = f.read()
            f.close()
        foods = lines[52:-964].split(" ")
        print(random.choice(foods))
    else:
        # make first request to the url in order to retreive contents
        response = requests.get("https://en.wikipedia.org/wiki/List_of_breakfast_foods")
        data = response.text

        # retreive a list of all of the food items
        soup = BeautifulSoup(data, "html.parser")
        tags = soup.find_all("li")
        foods = [tag.string for tag in tags]
        foods = filter(lambda x: x != None, foods)

        with open("list.txt", "a") as f:
            [f.write(food) for food in foods]
            f.close()

if __name__ == "__main__":
    main()
