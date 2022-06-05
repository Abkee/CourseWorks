import random
# для работы с картинками
from PIL import Image
# для работы с интернетом
import requests as requests
from selenium import webdriver

#  настроим selenium
options = webdriver.ChromeOptions()
options.headless = True

# укажем путь для драйвера
driver = webdriver.Chrome(executable_path='./chromdriver/chromedriver.exe', options=options)

# для сохранения имя файлов
pictures = []

# Основная функция
def func():
    url = 'https://yandex.kz/images/search?text='
    matin = input('Мәтінді енгізіңіз: ')
    mas = matin.split()

    # мәтінді форматтаймыз
    if len(mas) == 0:
        print('Сіз ешқандай мәтін енгізбедіңіз')
        return
    elif len(mas) == 1:
        url += mas[0]
    else:
        for t in range(len(mas)):
            if t != 0 or t != len(mas) - 1:
                url += '%20' + mas[t]
            else:
                url += mas[t]
    # Егер бәрі дұрыс болса суретты іздеуге кірісеміз
    try:
        driver.get(url=url)
        images = driver.find_elements_by_tag_name('img')
        n = 0
        for image in images:
            # сурет саны өзшертуге (болады)
            if n == 5:
                break
            #print(image.get_attribute('src'))

            # Вызываем функция для сохранения
            down_image(image.get_attribute('src'))
            n = n + 1
    # если есть ошибки
    except Exception as ex:
        print(ex)
    # закрываем драйвер
    finally:
        driver.close()
        driver.quit()


# для сохранения картинок
def down_image(url):
    # генерируем случайное имя для картинок
    name = 'qwertyuiopasdfghjklkzxcn'
    nam = ''
    for i in range(5):
        nam += random.choice(name)
    try:
        response = requests.get(url=url)

        with open(f'./files/{nam}.jpg', 'wb') as file:
            file.write(response.content)
            pictures.append(nam+'.jpg')

    except Exception as ex:
        return 'Не удалось скачать'


# Показываем случайную картинку которое мы сохраняли
def open_image(name):
    img = Image.open(f'./files/{name}')
    img.show()


# Точка входа в программу
if __name__ == '__main__':
    func()
    open_image(random.choice(pictures))

