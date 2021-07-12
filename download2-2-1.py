import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2F4b%2F09%2F62%2F4b09628c4e24e141eb2f7d0c2b036d52--cute-cats-big-cats.jpg&type=a340"
htmlUrl = "http://google.com"
print('Hi')
savePath1 = "c:/python/section2/test1.jpg"
savePath2 = "c:/python/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료!")
