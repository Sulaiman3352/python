# Git link from anime4up website 

# 1st step import modules 

import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 
import collections  
import urllib.request

anime_name_list = []
anime_link_list = []
down_link = [] 

# 2nd step use requests to fetch the url 
page_num = 1 
while True:
    result = requests.get(f"https://ww.anime4up.com/episode/boruto-naruto-next-generations-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-{page_num}/")

# 3rd step save page content/markup 

    src = result.content

# 4th step create soup object to parse content 

    soup = BeautifulSoup(src, "lxml")

    if page_num > 187 : 
        print(" finished stage 1 of 2 ")
        break 

# 5th step find the elements contanining info we need 
    # anime name + episode number , link 

    anime_name = soup.find_all("title")
    anime_link = soup.find_all("a",  text="4shared")
          
    emp = []
    print(" page switched "+ str(page_num) )
    page_num += 1 
     
    # other website 
    a = "vidbm"
    b = "uptostream" 

    if str(anime_link) == str(emp): 
    # git link from other host website 
        anime_link = soup.find_all("a",  text="vidbm") 
        if a in str(anime_link) :
            for i in range(len(anime_name)) :
                anime_name_list.append(anime_name[i].string)

                link = str(anime_link)[17:-26].replace('embed-', '') 
                anime_link_list.append(link) 

            for item in anime_link_list:
                result = requests.get(link) 
                src = result.content 
                soup = BeautifulSoup(src, "lxml") 
                downl_link = soup.find("video", {"class":"jw-video jw-reset"}) 
                down_link.append(downl_link['src']) 

        else :
            anime_link = soup.find_all("a",  text="uptostream") 

        continue 
    else:
        pass 
# 6th step loop over returned lists to exract needed info other lists 

        for i in range(len(anime_name)) :
            anime_name_list.append(anime_name[i].string)
            # convert list to string and Extract Link 
            an = str(anime_link[0]) 
            
            an2 = an.split() 
            an3 = an2[1]
            link = an3[13:-1] 
            anime_link_list.append(link)
        
     
            

for item in anime_link_list:
    result = requests.get(link) 
    src = result.content 
    soup = BeautifulSoup(src, "lxml") 
    downl_link = soup.find("source", {"type":"video/mp4"}) 
    down_link.append(downl_link['src']) 

#    anime_link_list.append(anime_link[i].find("a").attrs['data-ep-url'])   
 

#7th step create csv file and fill it with values 

file_list = [anime_name_list, anime_link_list, down_link] 
exported = zip_longest(*file_list) 
with open("/Users/sulai/Documents/Boruto_link.csv", "w") as myfile: 
#with open("/home/salomy/Documents/Boruto_link.csv", "w") as myfile: 
    wr = csv.writer(myfile) 
    wr.writerow(["Anime name and episode number", "Page Link for video", "download link for video"])
    wr.writerows(exported)  

print(" finished stage 2 of 2 ") 

#8th step to fetch the - of the job and fetch in page details


#9th step download episode from link 

#for i in anime_name_list :
#    urllib.request.urlretrieve(down_link[0] , anime_name_list[0] ) 
#    i+=1

#