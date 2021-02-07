# Git link from anime4up website 

# 1st step import modules 

import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 

anime_name_list = []
anime_link_list = []

# 2nd step use requests to fetch the url 

result = requests.get("https://ww.anime4up.com/episode/boruto-naruto-next-generations-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-1/")

# 3rd step save page content/markup 

src = result.content

# 4th step create soup object to parse content 

soup = BeautifulSoup(src, "lxml")

# 5th step find the elements contanining info we need 
# anime name + episode number , link 

anime_name = soup.find_all("title")
anime_link = soup.find_all("a",  text="4shared")
an_l = anime_link.find("a").attrs['data-ep-url'] 
print(an_l) 

# 6th step loop over returned lists to exract needed info other lists 

for i in range(len(anime_name)) :
    anime_name_list.append(anime_name[i].string)
# convert list to string and Extract Link 
#    an = str(anime_link[0]) 
#    an2 = an.split() 
#    an3 = an2[1]
#    anime_link_list.append(an3[13:-1])
# 

    anime_link_list.append(anime_link[i].find("a").attrs['data-ep-url'])   
    print(anime_name_list,anime_link_list) 

#7th step create csv file and fill it with values 

#file_list = [anime_name_list, anime_link_list] 
#exported = zip_longest(*file_list) 
#with open("/Users/sulai/Documents/Boruto_link.csv", "w") as myfile: 
#    wr = csv.writer(myfile) 
#    wr.writerow(["Anime name and episode number", "Page Link for video"])
#    wr.writerows(exported)  

#8th step to fetch the - of the job and fetch in page details


