from requests import get
from bs4 import BeautifulSoup
from tabulate import tabulate
import os

def fetch_table():
    try:
        corona_web_url = 'https://www.mohfw.gov.in/'
        html_text = get(corona_web_url).text
        html_text = BeautifulSoup(html_text, 'html.parser')
        new_table = html_text.find("div", class_ = "data-table").table
        datafile = open("index.html", "r")
        data = datafile.read()
        temp = data.split("??")
        data = str(temp[0]) + str(new_table) + str(temp[1])
        datafile.close()
        datafile = open("index.html", "w")
        datafile.write(data)
        datafile.close()
    except ConnectionError:
        print("Network Problem..")
        print("Try to checkout your internet connection")
    except:
        print("\n")
    return

fetch_table()
