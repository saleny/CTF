from PIL import Image

def gorizont(num, num1):
    img = Image.new('RGB', (10, 500))
    itog = num + 50
    while num<itog:
        num = num + 1
        number = 'img' + str(num)
#        print(number)
        number = Image.open(str(num)+'.jpg')
#    number.show()
        img.paste(number, (0, 0+num1))
        num1 = num1 + 10
#    img.show()
    img.save('d:\\1\\'+str(num)+'.jpg')

def vertical (num,num1):
    img = Image.new('RGB', (600, 500))
    while num<=2940:
        num = num + 50
        number = 'img' + str(num)
        print(number)
        number = Image.open('d:\\1\\'+str(num)+'.jpg')
#    number.show()
        img.paste(number, (0 +num1, 0))
        num1 = num1 + 10
#    img.show()
    img.save('d:\\1\\itog.jpg')

num = 0
while num<=2999:
    gorizont(num, 0)
    num = num + 50

vertical(0,0)
