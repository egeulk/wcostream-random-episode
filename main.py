# This is a sample Python script.
import random
import webbrowser
#lxml is also a dependency
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests


def main(name):
    with open("links") as file:
        lines = [line.rstrip() for line in file]
        if len(lines) == 0:
            raise Exception("File is empty")
    randomShowIndex = random.randint(0, len(lines) - 1)
    html_text = requests.get(lines[randomShowIndex])
    soup = BeautifulSoup(html_text.text, 'lxml')
    episodes = soup.find('div', class_='menustyle').find_all('a')
    randomEpisodeIndex = random.randint(0, len(episodes) - 1)
    randomEpisode = episodes[randomEpisodeIndex]
    randomEpisodeLink = randomEpisode['href']
    webbrowser.open(randomEpisodeLink, new=0, autoraise=True)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
