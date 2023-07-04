import requests

from bs4 import BeautifulSoup
import time


def control():
    URL='https://www.amazon.com.tr/dp/B0BH4J5YCQ/?_encoding=UTF8&pd_rd_i=B0BH4J5YCQ&ref_=sbv_store_search&pd_rd_w=aelxH&content-id=amzn1.sym.443bd00b-bbee-46f4-9420-427b1751bc7a%3Aamzn1.sym.443bd00b-bbee-46f4-9420-427b1751bc7a&pf_rd_p=443bd00b-bbee-46f4-9420-427b1751bc7a&pf_rd_r=YY8BBXCDQBXW5WRC1Q9F&pd_rd_wg=G4ARG&pd_rd_r=64a93300-613e-4794-9bc1-9fa12fae1212&&pd_rd_plhdr=t'

    myUserAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    connection = requests.get(URL , headers = myUserAgent)

    content = BeautifulSoup(connection.content,'html.parser')

    productName = content.find(id='productTitle').get_text().strip()

    price = content.find("span",class_="a-price-whole").get_text()
   

    newPrice=int(price[0:6].replace('.',''))

    print(productName)
    print(newPrice)
 
control()




