import requests as r

while True:
 k=input("me:")
 f=r.get("http://sandbox.api.simsimi.com/request.p?key=b1d9f4c3-28ad-4709-8067-8c5c68d2112a&lc=vn&ft=1.0&text="+k).json()
 print("it:"+f["response"])
