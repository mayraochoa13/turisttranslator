from bs4 import BeautifulSoup
import urllib

myurl= "https://www.engadget.com/2017/04/06/the-ubuntu-mobile-dream-is-over/"
readInStuff = urllib.urlopen(myurl).read()

#print readInStuff[0:25]
soup = BeautifulSoup(readInStuff, "html.parser")
#print soup.prettify()[1000:1100]

print soup.title.getText()
for link in soup.find_all('a'):
    print link.get('href')
