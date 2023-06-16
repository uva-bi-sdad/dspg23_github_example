import csv
import requests
from bs4 import BeautifulSoup

global url

#it's not a very good tool because if the url is not from yelp, it wont work, however it serves its purpose  temporarily
#the site might not have 220 pages with data so this would need to be automated
i = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220]

filename = 'yelp_minority_directory.csv'
with open(filename, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'URL'])

    for page in i:
        url = 'https://www.yelp.com/search?find_desc=Minority+Owned&find_loc=Fairfax%2C+VA&start=' + str(page)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # if the website changes then the tags have to change
        div_elements = soup.find('ul', {'class': 'undefined list__09f24__ynIEd'})

        for div_element in div_elements:
            name_element = div_element.find('span', {'class': 'css-1egxyvc'})
            url_element = div_element.find('a')
        # add a warning if nothing is found because it could be that the website made some changes
            if name_element is not None and url_element is not None:
                name = name_element.get_text(strip=True)
                url = url_element['href']

                writer.writerow([name, url])

print('Success!')
#list ideas in a group setting
#brainstorm
#try things out