
file1 = open('file1.txt', 'w')
text = 'look at how beautiful this world '
file1.write(text)
file1.close()

with open('file1.txt') as f:
    file1 = [word for line in f for word in line.split()]
    print(file1)

for x in file1:
    if x == 'world':
        # print(x)
        with open('file2.txt', 'w') as f2:
            f2.write(x)
            print(f2)


""" Задание 2"""


import json
my_json = {
   "article": [

      {
         "id" : "01",
         "language" : "rus",
         "edition" : "first",
         "author" : "Pushkin"
      },

      {
         "id":"02",
         "language": "eng",
         "edition": "second",
         "author": "Shekspir"
      }
   ]

}

testJson = json.dumps(my_json, indent=4)
with open('test.json', 'w') as file:
    file.write(testJson)
    print(testJson)