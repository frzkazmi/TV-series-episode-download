import wget
import urllib2
from bs4 import BeautifulSoup
from subprocess import call

idmPath = "C:\Program Files (x86)\Internet Download Manager\IDMan.exe"
site1="http://dl.tehmovies.com/94/series/"
hdr = {'User-Agent': 'Mozilla/5.0'}
url2=[]
def parse(url):
	
    req = urllib2.Request(url,headers=hdr)
    homePage = urllib2.urlopen(req)
    homePageSoup = BeautifulSoup(homePage,'lxml')
    Results = homePageSoup.find("pre")
    name=Results.find_all("a")
    links=Results.find_all('a[]')
    
     
    for i, j in enumerate(name):
            print str(i)+" "+j.text.encode("utf-8")
            url2.append(j.text.encode("utf-8"))
    print "---------------------------------------------------"	
    	
def Again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to donload any more episode? (yes or no)')
    return raw_input().lower().startswith('y')

while True:
    
    
          
    parse(site1)            
    index1=int(raw_input("Enter the index of tv show:"))
    url3=site1+url2[index1]
    url2=[]
    print "Now showing list of all seasons...."
    parse(url3)
    index2=int(raw_input("Enter index of the season: "))
    url4=url3+url2[index2]
    print url4
    
    print "Now showing list of all episodes of this season:"
    parse(url4)
    index3=int(raw_input("Enter index of the season: "))

    file_url=url4+url2[index3]
    episode_name=""
    print file_url
    print "Downloading the episode..."
    episode_name+=url2[index3]
    downloader_choice=int(raw_input("How do you want to download movie? 1: Through idm  2:Through wget"))
    if downloader_choice==1:
            call([idmPath, "/d", file_url, "/n", "/s", "/f",  episode_name + '.mp4'])
    elif downloader_choice==2:
            file_name = wget.download(file_url)
    url2=[]        
    if not Again():
        break

