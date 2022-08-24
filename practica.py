# import sys
# import ssl
# from urllib import request
#
#
# def downloadFile():
#     ssl._create_default_https_context = ssl._create_unverified_context
#
#     fileName = 'generated.json'
#     urlFile = 'https://cloud.it-stepbystep.ru/s/tciPs29rFjxrHpm/download/generated.json'
#     headerUrl = {
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#         'Accept-Encoding': 'none',
#         'Accept-Language': 'en-US,en;q=0.8',
#         'Connection': 'keep-alive'}
#
#     try:
#         url = request.Request(urlFile, None, headerUrl)
#         page = request.urlopen(url)
#         f = open(fileName, 'wb')
#         f.write(page.read())
#         f.close()
#     except Exception:
#         print(sys.exc_info()[1])
#         exit()
#
#
# downloadFile()


# 1.
import json

jsonDocument = 'generated.json'

f = open(jsonDocument, 'r')
jsonData = json.load(f)
f.close()

personList = []
for x in jsonData:
    print("User id: ", x['_id'])
    print("User name: ", x["name"])
    print("User age: ", x["age"])
    print("User gender: ", x["gender"])
    print("User balance: ", x["balance"])
    print("User email: ", x["email"])
    print("User phone: ", x["phone"])
    print("User isActive: ", x["isActive"])
    print("*" * 30)
    information = {

        "_id": x['_id'],
        "name": x["name"],
        "age": x["age"],
        "gender": ["gender"],
        "balance": x["balance"],
        "email": x["email"],
        "phone": x["phone"],
        "isActive": x["isActive"]

    }

    personList.append(information)



f = open('result.txt', 'w')
personList.sort(key=lambda row: row["isActive"])
text = str(personList)
f.write(text)
f.close()
print(personList)


f = open('result1.txt', 'w')

ListPersonTrue = list(filter(lambda row: row["isActive"] == True, personList))

ListPersonTrue.sort(key=lambda row: row['balance'], reverse=True)

text = str(personList)
f.write(text)
f.close()
print(personList)
for x in ListPersonTrue:
    print(x)