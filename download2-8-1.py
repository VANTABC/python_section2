from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()

opener.addheaders = [('User-agent', 'Mozilla/5.0')]

req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath = "C:/python/img_down"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 시패!")
        raise

soup = BeautifulSoup(res, "html.parser")
print(soup)
img_list = soup.select("div.thumb > a.link_thumb._imageBox._infoBox > img")
print("test", img_list)
