"""
  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !

  These are didactic files, they are with a lots of comments to be consulted at some point 

  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
"""
from bs4 import BeautifulSoup

with open('index.html', 'r') as Condor_html_website:
    # content = variable.read()
    # # print(content) 

    # soup = BeautifulSoup(content, 'lxml')
    # # print(soup.prettify()) 
    # # it printds the html code just like the previously print(content) does
    
    # # seaching for a specific html tag, this only finds the first occourrence
    # tags =  soup.find('li')
    # print('the first occourence of a li tag is:' ,tags)

    # # # seaching for a specific html tag, this finds all the occourrences
    # tags2 = soup.find_all('li')
    # # print('all the occourences of a li tag are:' ,tags2)

    # for lis in tags2:
    #     print(lis.text)


    content = Condor_html_website.read()
    # parser:
    soup = BeautifulSoup(content , 'lxml') 

    # products_price = soup.find_all('p', class_='regular')
    # print(products_price)
    # for price in products_price:
    #     print(price.text)

    product = soup.find_all('div', class_='content')

    for product_features in product:
        print(product_features.text)


    # You can navigate through the html structure by usingf the '.' that is: product.p
    # This is going to get the <p></p> inside product

