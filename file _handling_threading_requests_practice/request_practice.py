import requests
# GET REQUEST

r = requests.get('https://stackoverflow.com/questions/49191883/get-number-of-bytes-during-a-request',  headers={'User-Agent': 'Mozilla/5.0'})


print(r.status_code)
print(r.headers['content-type'])
print(r.headers)
# print(r.headers['content-length'])
print(len(r.content))
print(r.headers['transfer-encoding'])
print(r.content.json)
# if using HTTP basic auth :
# pass in the get method : auth=('user', 'pass')
# requests.get('https://api.github.com/user', auth=('user', 'pass'))


# POST REQUEST
# payload = {'key1': 'value1', 'key2': 'value2'}
# >>> r = requests.post("http://httpbin.org/post", data=payload)

# FOR SENDING FILES,
# url = 'http://httpbin.org/post'
# files = {'report.xls': open('report.xls', 'rb')}
# r = requests.post(url, files=files)
