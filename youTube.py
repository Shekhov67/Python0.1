'''from turtle import *
pensize(20)

while True:
    forward(10)
    left(10)

exitonclick()'''

''''Убрать фон
установщик pip install rembg

'''
from rembg import remove
from PIL import Image

input_path = 'C:\\Users\\shehs\\OneDrive\\Desktop\\1.jpg'
output_path = 'C:\\Users\\shehs\\OneDrive\\Desktop\\output_3.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)