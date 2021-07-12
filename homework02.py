from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.naver.com/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")


top = soup.select("ul.list_eventlist_event")
print(top)
#for i,e in enumerate(top,1):
    #print(i,e.select_one("h4.block_title > a").string)
