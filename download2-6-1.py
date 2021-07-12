from bs4 import BeautifulSoup
import sys
import io
import re   #정규표현식 사용을 위한 임포트

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a id = "naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").string) #id값으로 확인
li1 = soup.find_all(href = re.compile(r"^https://")) #https://로 시작하는 것 확인(정규표현식)
li2 = soup.find_all(href = re.compile(r"da")) #문자열 da를 포함하는 것 확인(정규표현식)

for e1 in li1:
    print(e1.attrs['href'])

for e2 in li2:
    print(e2.attrs['href'])
