import requests
file = open("E:\\github\\hotelapp\\static\\bulks\\test1\\test2.png","w")
r = requests.post(url, files=files)
#print("\\static\\IMAGES\\11.jpg",file=file)