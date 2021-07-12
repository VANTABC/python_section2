from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
#print('soup', type(soup))
#print('prettify', soup.prettify())

h1 = soup.html.body.h1
print('h1', h1)
print(h1.string)

p1 = soup.html.body.p
print('p1', p1)     #요렇게 하면 태그선택자만 가져오게 된다, 난 CSS선택자를 가져오고 싶은데...
p2 = p1.next_sibling        #next_sibling을 사용하면 같은 레벨의 다음 노드를 가져올수 있는...
print('p2', p2)     #어? 왜 안되지? -> 줄바꿈때문!
p3 = p1.next_sibling.next_sibling
print('p3', p3)
p4 = p1.previous_sibling.previous_sibling
print('p4', p4)

print("h1 >> ", h1.string)
print("p >> ", p1.string)
print("줄바꿈 >> ", p2.string)
print("p >> ", p3.string)
print("h1 >>", p4.string)
