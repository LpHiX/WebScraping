import requests
from bs4 import BeautifulSoup



def main():
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='ResultsContainer')
    job_elements = results.find_all("div", class_="card-content")
    for job_element in job_elements:
        print(job_element.find("h2", class_="title").text)
        print(job_element.find("h3", class_="company").text)
        print(job_element.find("p", class_="location").texxt)
        print()

def main2():
    URL = "https://www.timeanddate.com/weather/hong-kong/hong-kong/ext"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(id="wt-ext")
    rows = table.find_all("tr")
    for row in rows:
        print(row.find)

if __name__ == '__main__':
    main2()
