import urllib.request

storage_path = 'C:/Users/XXX/Desktop/'# e.g. C:\Users\XXX\Desktop\

file_list="/distribution/image-data/list.txt"
signature="?email=m0634194@mail.fcu.edu.tw&Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6ICJodHRwczovL25pY28tb3BlbmRhdGEuanAvZGlzdHJpYnV0aW9uLyo~ZW1haWw9bTA2MzQxOTRAbWFpbC5mY3UuZWR1LnR3IiwgIkNvbmRpdGlvbiI6IHsiRGF0ZUxlc3NUaGFuIjogeyJBV1M6RXBvY2hUaW1lIjogMTU0NDU4NDQ4Mn19fV19&Signature=j2F3N71C~9yTVFOR9vUFuhUZ0ndlrz~3hevW584A3u3JmzywTNCUSUJSmAsR-dDiiBfP~B8mzZYZhE5ePhPVspCREl7c-htWVlrtDyjgzxmKOZ0NmerAg93y~ACM3PW0yWs3Ow~UfJd09~b-EnexvG6lNDgJBvh~phEZZCCszWT6O2Gv-Nb3G5Vuv6QrWB-SIq4N8PjZk2MBvvyTibLKeRlfzN1ew1-vSffVQqSCCjovIwsCOlWCkYggo~u9xGjN85vavySzRjnPd2Ykfsq-r~dGRPtoT8QzeBzoy4mLL6EvPakV6jwYQ0GsH2oM0lxo3wrvdlwWLsy9DMck49cEJw__&Key-Pair-Id=APKAINZSYXWBRMHNWVQA"
origin="https://nico-opendata.jp"
print('downloading with urllib') 
url_list, _ =urllib.request.urlretrieve(origin + file_list + signature)
f = open(url_list, 'r')
i=0
for item in f.readlines():
	item=item.strip('\n')
	urllib.request.urlretrieve(origin + item + signature,storage_path + '%s.zip'%i)

	i=i+1
#for item in file_list:
#urllib.request.urlretrieve(url, "demo.zip")
