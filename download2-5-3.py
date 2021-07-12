from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")  #전체를 다 가져옴
#print('links', type(links))

a = soup.find_all("a",string="daum")    #daum을 포함한것만 가져옴
print('a',a)

b = soup.find("a")  # 가장 상위의 하나만 가져옴
print('b',b)

c = soup.find_all("a", limit=3) # 제한을 걸어서 limit에 할당된 숫자만큼만 가져온다
print('c',c)

d = soup.find_all(string=["naver", "google"])
print('d',d)

for a in links:
    #print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    #print('txt >> ', txt, 'href >> ', href)
