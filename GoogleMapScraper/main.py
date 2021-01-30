# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# imports
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()


company_name=[]
contact_List=[]
location_list=[]

driver.get("https://www.google.com/maps/search/tuition/@19.8826384,75.0940323,9.96z")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('div',  attrs={'class': 'section-result-text-content'}):
        name=a.find('h3',attrs={'class': 'section-result-title'}).find('span')
        contact=a.find('span',attrs={'class': 'section-result-info section-result-phone-number'}).find('span')
        location=a.find('span',attrs={'class':'section-result-location'})
        print(name.text)
        company_name.append(name.text)
        print(location.text)
        location_list.append(location.text)
        print(contact.text)
        contact_List.append(contact.text)
        print("\n")

    df = pd.DataFrame({'Institute Name': company_name, 'Contact': contact_List, 'Address': location_list})
    df.to_csv('leads.csv', index=False, encoding='utf-8')
    driver.quit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
