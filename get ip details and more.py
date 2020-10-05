import socket as s
import IPToolz as ip 
# print(dir(ip))

website = 'gbprat.com'

#get local ip address
print(ip.getlocal())

#get website ip address
print(ip.getIP(website))

a = ip.getIP(website)
#get ip type
# print(ip.IPType(a))

#socket module using from here
hostname = s.gethostname() #computer name
a = s.gethostbyname(hostname) #computer ip address
print(a)

