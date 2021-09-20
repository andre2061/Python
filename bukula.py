import requests
from bs4 import BeautifulSoup
#!pip install pandas --quiet
import pandas as pd

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
#doc = get_topics_page(base_url + a_tags[1]['href'])
doc = base_url + a_tags[1]['href']
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
