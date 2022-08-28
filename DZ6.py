
myText = []
myNum = []
myList = []

def main():

    myList.append(int(input('Ведите чило:   ')))
    myList.append(str(input('Ведите слово:   ')))
    myList.append(int(input('Ведите число:   ')))
    print(myList)
    for element in myList:
        if type(element) is int:
            myNum.append(element)
        elif type(element) is str:
            myText.append(element)
            print("Список слов: ", *myText)
            print("Список цифр: ", *myNum)


if __name__ == '__main__':
    main()

""" Задание 2"""

from random import sample

list = sample(range(1, 500), 20)
print(list)
print(max(list))
print(min(list))