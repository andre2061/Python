import requests
from bs4 import BeautifulSoup
#!pip install pandas --quiet
import pandas as pd

def get_topics_page():
    topics_url = 'http://books.toscrape.com/'
    response = requests.get(topics_url)
    page_contents = response.text
    doc = BeautifulSoup(page_contents, 'html.parser')
    return doc
topics_page = get_topics_page()
type(topics_page)
topics_page.find('a')
def extract_book_links(doc):
    h3_tags = doc.find_all('h3')
    book_links = []
    base_url = "http://books.toscrape.com/"

    for tag in h3_tags:
        book_links.append(base_url + tag.contents[0]['href'])

    return book_links
links = extract_book_links(get_topics_page())
links[:4]
def get_book_topics(doc):
    h3_tags = doc.find_all('h3')
    book_titles = []
    for tag in h3_tags:
        book_titles.append(tag.text)
    return book_titles
topics = get_book_topics(get_topics_page())
topics[:4]
def get_book_prices(doc):
    p_tags = doc.find_all('p', {'class': 'price_color'})
    book_prices = []
    for tag in p_tags:
        book_prices.append(tag.text)
    return book_prices
price = get_book_prices(get_topics_page())
price[:4]
def get_book_availability(doc):
    i_tags = doc.find_all('p', {'class': 'instock availability'})
    book_availability = []

    for tag in i_tags:
        book_availability.append(tag.text.strip())

    return book_availability
get_book_availability(get_topics_page())[4]
def get_book_types(doc):
    li_tags = doc.find_all('a')
    book_types = []
    base_url = "http://books.toscrape.com/"
    for tag in li_tags:
        book_types.append(base_url + tag['href'])
    return book_types
book_types_links = get_book_types(get_topics_page())[3:]
book_types_links
a=[]
b=[]
for link in book_types_links:
    response = requests.get(link)
    doc_link = BeautifulSoup(response.text, 'html.parser')
    tags = doc_link.find_all('strong')
    for tag in tags:
        if tag == 0:
            print(tag.text)
#!pip install pandas --quiet
import pandas as pd
topics_dict = {
    'Title' : get_book_topics(get_topics_page()),
    'Link' : extract_book_links(get_topics_page()),
    'Availability' : get_book_availability(get_topics_page()),
    'Price' : get_book_prices(get_topics_page())
}
topics_df = pd.DataFrame(topics_dict)
topics_df.head()                        
def scrape_main_page():
    doc = get_topics_page()
    book_links = extract_book_links(doc)
    book_titles = get_book_topics(doc)
    book_prices = get_book_prices(doc)
    book_availability = get_book_availability(doc)
    
    topics_dict = {
    'Title' : book_titles,
    'Link' : book_links,
    'Availability' : book_availability,
    'Price' : book_prices
    }
    topics_df = pd.DataFrame(topics_dict)
    print('The .csv file for home page is being Created.')
    topics_df.to_csv('topics.csv', index = None)
    scrape_main_page()
def scrape_links_for_topic_page(doc):
    list_tag = doc.find('ul',class_='nav nav-list')
    li = list_tag.find_all('li')
    a_tags = li[0].find_all('a')
    hrefs = []
    for tag in a_tags:
        hrefs.append(tag.get('href'))
    booktopic_links = []
    base_url = "http://books.toscrape.com/"

    for tag in hrefs:
        booktopic_links.append(base_url + tag)
    return booktopic_links
def scrape_topic_of_the_book(booktopic_links):
    a = []
    for i in booktopic_links:   
        response = requests.get(i)
        topic_doc = BeautifulSoup(response.text, 'html.parser') #Parse all the page
        div_tags = topic_doc.find_all('strong')
        strong = []
        for i in div_tags:
            strong.append(i.text)
        a.append(strong[0])
    return a
def scrape_number_of_books(booktopic_links):
    b = []
    for i in booktopic_links:   
        response = requests.get(i)
        topic_doc = BeautifulSoup(response.text, 'html.parser') #Parse all the page
        div_tags = topic_doc.find_all('strong')
        strong = []
        for i in div_tags:
            strong.append(i.text)
        b.append(strong[1])
    return b

doc = get_topics_page()
booktopic_links = scrape_links_for_topic_page(doc)
topics = {
    'Topic' : scrape_topic_of_the_book(booktopic_links),
    'Number Of Books' : scrape_number_of_books(booktopic_links) 
}
c = pd.DataFrame(topics)[1:]
c.head()  
csv_data = c.to_csv('Number_of_books_in_each_topic.csv', index=False) 
print("The .csv file about books of each topic is being created...")

def scrapeTopics():
    doc = get_topics_page()
    booktopic_links = scrape_links_for_topic_page(doc)
    topics = {
        'Topic' : scrape_topic_of_the_book(booktopic_links),
        'Number Of Books' : scrape_number_of_books(booktopic_links) 
    }
    c = pd.DataFrame(topics)[1:]
    c
    csv_data = c.to_csv('Number_of_books_in_each_topic.csv', index=False) 
    print("The .csv file about books of each topic is being created...")
    
scrapeTopics()
#!pip install jovian --upgrade --quiet
import jovian
# Execute this to save new versions of the notebook
jovian.commit(project="scraping_books_website")
def extract_book_links(doc):
    h3_tags = doc.find_all('h3')
    book_links = []
    base_url = "http://books.toscrape.com/"

    for tag in h3_tags:
        book_links.append(base_url + tag.contents[0]['href'])

    return book_links

def extract_table_heads(topic_doc):
    desc_tags = topic_doc.find_all('th')                    
    desc = []                                              
    for tag in desc_tags:
        desc.append(tag.text)
        
    return desc
def extract_table_data(topic_doc):
    tabledata_tags = topic_doc.find_all('td')
    tbdata = []                                             
    for tag in tabledata_tags:                  
        tbdata.append(tag.text)
        
    return tbdata
def extract_paragraph(topic_doc):
    div_tags = topic_doc.find('div',{'class':'content'})
    para_tags = div_tags.find_all('p')
    
    return para_tags[3].text
def extract_title_of_books(topic_doc):
    tit_tag = topic_doc.find('h1')
    return tit_tag.text
def csv_home_pag(book_links):
    list = []
    list1 = []
    list2 = []
    for i in book_links:                                        
        response = requests.get(i)
        topic_doc = BeautifulSoup(response.text, 'html.parser')                                           
        table = dict(zip( extract_table_heads(topic_doc), extract_table_data(topic_doc)))
        list.append(table)   
        list1.append(extract_paragraph(topic_doc))
        list2.append(extract_title_of_books(topic_doc))
    df = pd.DataFrame(list)
    df.pop('Product Type')
    df1 = pd.DataFrame(list1,columns =['Description'])
    df2 = pd.DataFrame(list2,columns =['Title'])
    final = pd.concat([df2,df1,df],axis=1)
    csv_data = final.to_csv('csv_data.csv', index=False) 
    return final
csv_home_pag(extract_book_links(doc)).head()
csv_home_pag(extract_book_links(doc))
section = doc.find('li',{'class':'next'})
next_url = section.contents[0]['href']
base_url = "http://books.toscrape.com/"
a = base_url + next_url
response = requests.get(a)
page_contents = response.text
doc1 = BeautifulSoup(page_contents, 'html.parser')
csv_home_pag(extract_book_links(doc1))  

