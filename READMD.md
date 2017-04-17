#This code is my school Taiyuan University of Technology Academic Office of the simulated login

##Use two way to simulated login my school acdaemic office.
###The first way cookie
```python
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
```

###The second way session
```python
s=requests.Session()
Post=s.post(loginUrl,headers=headers,data=datas)
```
