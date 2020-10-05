import am_i_connected as aic

# print(dir(aic))

if aic.CheckThereIsConnection() == True:
    print('you are connected boss')
    
else:
    print('bhai mere aap apna internet check kijiye')

# import requests as rq
# from am_i_connected import am_i_connected as aic
# import am_i_connected as aic
# # def check_internet():
# # 	res = False
# # 	try:
# # 		rq.get('https://www.google.com')
# # 		res = False
# # 		print("you are connected to Internet")
# # 	except Exception:
# # 		res = True
# # 	if res:
# # 		print("\n\n\tIt seems That your internet Speed is slow or Maybe You are useing proxies...")
# # 		print("\t\tHackerGprat Will Stop now\n\n\n")		
# # 		exit()
		
# # check_internet()


# #===================================================


# #about
# #pip install am-i-connected
