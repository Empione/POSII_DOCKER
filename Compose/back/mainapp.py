import tensorflow as tf
import PIL.ImageOps
import numpy as np
from PIL import Image
import socket
import time

test_model = tf.keras.models.load_model('Model_NN.h5')

Clothes = {0: 'T-Shirt категория 0', 1: 'Trouser категория 1',
           2: 'Pullover категория 2', 3: 'Dress категория 3',
           4: 'Coat категория 4', 5: 'Sandal категория 5',
           6: 'Shirt категория 6', 7: 'Sneaker категория 7',
           8: 'Bag категория 8', 9: 'Ankle_boot категория 9'}

sock = socket.socket()
sock.bind(('', 9090))


def img_prep(i):
    img = Image.open(i).convert('L').resize((28, 28))
    inverted_image = PIL.ImageOps.invert(img)
    arr_image = np.array(inverted_image).reshape(1, 28, 28) / 255.0
    return arr_image


def pred(i):
    load_image = img_prep(i)
    predictions = test_model.predict(load_image)
    result = np.argmax(predictions)
    a = Clothes.get(result)
    return a

while True:
    while True:
        sock.listen(1)
        conn, addr = sock.accept()
        data = conn.recv(1024)
        if not data:
            break
        time.sleep(1)
        a = pred(data)
        time.sleep(1)
        print('\n\n**********************************')
        print('*  '+a)
        print('**********************************')
        
