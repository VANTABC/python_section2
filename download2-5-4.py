from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class = "lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select("div#main > h1")   # 이렇게 하면 리스트로 반환이 되어서 for문을 돌려서 출력해야한다
for z in h1:
    print("h1", z.string)

h2 = soup.select_one("div#main > h1")   # 이렇게 하면 한개만 반환이 되므로 바로 출력가능
print("h2", h2.string)

list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>>", li.string)
