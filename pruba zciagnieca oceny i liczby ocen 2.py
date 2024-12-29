from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
import re


MAIN_URLS = [
    "https://www.filmweb.pl/ranking/film/country/42"

]


film_data = []

for MAIN_URL in MAIN_URLS:
    try:
        response = requests.get(MAIN_URL)

        main_website = BeautifulSoup(response.text, "html.parser")
            
           
        ranking_elements = main_website.find_all("div", class_="rankingType rankingType--odd")
            
        for element in ranking_elements:
            dream = random.randint(1,5)
            title = element.text.strip()  
            film_data.append( title)
            print("loading.........")
                # if dream == 2 or dream == 4:
                #     time.sleep(3)

    except Exception as e:
        print(f"Wystąpił błąd podczas przetwarzania {MAIN_URL}: {e}")





film_data = [re.sub(r'https://\S+', '', item).strip() for item in film_data]
print(film_data)


import pandas as pd
import re
pattern = r"""
    (?P<title>.+?)               
    (?P<year>\d{4})             
    \s                          
    (?P<rating>\d{1,2},\d{2})    
    \s10\s                       
    (?P<votes>[\d\s]+)           
"""


film_df = pd.DataFrame(film_data, columns=["raw_data"])

film_df = film_df["raw_data"].str.extract(pattern, flags=re.VERBOSE)


film_df["votes"] = film_df["votes"].str.replace(" ", "", regex=False).astype(int)


film_df["rating"] = film_df["rating"].str.replace(",", ".").astype(float)

film_df["year"] = film_df["year"].astype(int)





output_path = r"C:\Users\Admin\Desktop\outpu\filmweb.csv"
film_df.to_csv(output_path, index=False)
print(f"Dane zapisano w pliku: {output_path}")
film_df.to_excel(r"C:\Users\Admin\Desktop\outpu\filmweb.xlsx")
import matplotlib.pyplot as plt
film_df = film_df.sort_values("votes", ascending=True)
graph = plt.barh(film_df["title"], film_df["rating"])
plt.show()

