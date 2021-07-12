import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.pinimg.com%2F736x%2F4b%2F09%2F62%2F4b09628c4e24e141eb2f7d0c2b036d52--cute-cats-big-cats.jpg&type=a340"
htmlUrl = "http://google.com"

savePath1 = "c:/python/section2/test1.jpg"
savePath2 = "c:/python/section2/index.html"

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb') # w: write, r : read, a : add
saveFile1.write(f1)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
