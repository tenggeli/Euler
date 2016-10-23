#coding:utf-8
import urllib2
import httplib
import urllib

class SpiderMain(object):
	"""docstring for SpiderMain"""
	#def __init__(self):
		#coding
	def creaw(self, root_url):
		req = urllib2.Request(root_url)
		req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
		req.add_header("Cookie",'d_c0="AEBAwryS9AmPTouCwBTehleje9c4zTrD5kY=|1463811851"; _za=ca3f98e1-a6f6-49cd-b794-6de5a093c624; _zap=b37cc280-3efd-43b2-ae8b-7fd56147514d; q_c1=a683095af3af488c80988902df7149a8|1474513333000|1463811851000; cap_id="NDk0Yjk0NGJhZWI4NDkxODljNTEwM2M3ZGQyYjY5Nzg=|1475560287|3b55652c69c2f43da10ea06bfcdeee78712d22ff"; l_cap_id="NDdkZDI0ZjkxMzllNDU2ZmJiMDMwZTc1MWI2YmMwNTE=|1475560287|f20c05508d200832193ac1c2a63e67e4b8817717"; login="OTQ0Mjc0MTNlZDcyNDE0MjgwOWRlMDhkZThjYTg4NWU=|1475560287|992fbd7d4b53952bb94617886637a8e645dbd8b3"; _xsrf=8303624aecad4b1920aa7c49ca80cbfa; __utma=51854390.525516098.1476586278.1476586278.1476586278.1; __utmb=51854390.10.10.1476586278; __utmc=51854390; __utmz=51854390.1476586278.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20121104=1^3=entry_date=20121104=1; a_t="2.0AABAldcZAAAXAAAAjnoqWAAAQJXXGQAAAEBAwryS9AkXAAAAYQJVTV_QGlgAtrc6NoObulHJ7W7jJRCXjG1qabLt7zLrQh0bCX2NHHflndxZbGqYqg=="; z_c0=Mi4wQUFCQWxkY1pBQUFBUUVEQ3ZKTDBDUmNBQUFCaEFsVk5YOUFhV0FDMnR6bzJnNXU2VWNudGJ1TWxFSmVNYldwcHNn|1476586894|d51796823bf8d3f3cbf0f07fff49071e91e0cc68')
		Request = urllib2.urlopen(req)
		res= Request.read()
		print res


if __name__ == "__main__":
	root_url = "https://www.zhihu.com/people/teng-ge-li"
	obj_spider = SpiderMain()
	obj_spider.creaw(root_url)
