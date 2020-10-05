import requests as rq

def getapi(pn,lim,cc):
	cc = str(cc)
	pn = str(pn)
	lim = int(lim)
	url = ["https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" +
			str(cc) + "&nod=4&phone=" + pn,"https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo="]