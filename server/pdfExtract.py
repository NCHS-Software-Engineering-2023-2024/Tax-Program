import requests 
from bs4 import BeautifulSoup
from csv import writer 
import pandas as pd

url = "https://www.irs.gov/publications/p17#d0e50213"
page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')
tables = soup.find_all("table")
results = tables[-13]


with open('server/tax.csv', 'w', newline = '',encoding = 'utf8') as f:
    thewriter = writer(f)

    data = [] 
    first_row_skipped = False


    for row in results.find_all('tr'):
        
        cols = row.find_all('td')
        if len(cols) == 0: 
            cols = row.find_all('th')
    
        
        cols = [ele.text.strip() for ele in cols]
        if (len(cols) == 6):
            for element in cols: 
                element = element.replace('"', '')
                print(element)
            data.append([ele.strip() for ele in cols if ele]) #gets rid of empty values
            if (first_row_skipped == True): 
                df = pd.DataFrame(data)
                df.to_csv('server/tax.csv', index = False)
            else: 
                headers = data.pop(0)
                first_row_skipped = True
        
    
        


          #{/*if (first_row_skipped == True): 
                #thewriter.writerow(data)
                #headers = data.pop(0)
            #else: 
                #headers = data.pop(0)
                #first_row_skipped = True*/}
                  

            


  
    
        


