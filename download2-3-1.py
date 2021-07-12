import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com/"

mem = req.urlopen(url)

#print(type(mem))

#print("geturl", mem.geturl())
#print("status", mem.status) #200(정상) 404(요청하는 페이지가 없음)
                            #403(내부망이 외부에서 접속불가)
                            #500(서버자체의 에러)
#print("headers", mem.getheaders())

#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50).decode("utf-8")) ##euc-kr ....
print(urlparse("http://www.encar.com/"))
