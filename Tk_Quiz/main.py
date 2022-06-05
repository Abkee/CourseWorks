from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

# json форматтағы файлмен жұмыс істеу үшін
import json


# Графикалық интерфейстің компоненттерін сипаттауға арналған класс
class Quiz:
    # Это первый метод, который вызывается, когда
    # инициализируется новый объект класса. Этот метод
    # устанавливает количество вопросов равным 0. и инициализирует все
    # # другие методы отображения содержимого и создания всех
    # доступные функциональные возможности
    def __init__(self):

        # cұрақтың номерін орнатамыз
        self.q_no = 0

        # Титлды және, сұрақтарды шығару функциялары
        self.display_title()
        self.display_question()

        # Вариантты таңдайтын айнымалы
        self.opt_selected = IntVar()

        # Варианттарды таңдау кнопкалары
        self.opts = self.radio_buttons()

        # Варианттарды шығару
        self.display_options()

        # Келесі және Аяқтау кнопкалары
        self.buttons()

        # сұрақтар болмаса
        self.data_size = len(question)

        # Дұрыс жауаптар счетчигі
        self.correct = 0

    # Тестті тапсырып болғасын
    # Результатты шығаратын функция
    def display_result(self):

        # Қате жауаптарды есептеу
        wrong_count = self.data_size - self.correct
        correct = f"Дұрыс жауаптар саны: {self.correct}"
        wrong = f"Қате жауаптар саны: {wrong_count}"

        # Дұрыс жауаптарды есептеу
        score = int(self.correct / self.data_size * 100)
        result = f"Балл : {score}%"

        # Результатты экранға шығару
        mb.showinfo("Результат", f"{result}\n{correct}\n{wrong}")

    # Этот метод проверяет ответ после того, как мы нажмем Next.
    def check_ans(self, q_no):

        # егер таңдалған вариант дұрыс болса
        if self.opt_selected.get() == answer[q_no]:
            return True

    # Этот метод используется для проверки ответа
    # текущий вопрос, вызвав функцию check_ans и номер вопроса.
    # если вопрос правильный, счетчик увеличивается на 1
    # а затем увеличить номер вопроса на 1. Если он последний
    # вопрос, то он вызывает результат отображения, чтобы показать окно сообщения.
    # иначе показывает следующий вопрос.
    def next_btn(self):

        if self.check_ans(self.q_no):
            # егер сұрақ дұрыс болса
            self.correct += 1

        # Счетчикты көбейтеміз, келесі сұраққа өту үшін
        self.q_no += 1

        # проверяет, равен ли размер q_no размеру данных
        if self.q_no == self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

        # Этот метод показывает две кнопки на экране.
        # Первая из них — кнопка next_button, которая переходит к следующему вопросу
        # У него есть такие свойства, как текст, который показывает функциональность,
        # размер, цвет и свойство текста, отображаемого на кнопке. Затем это
        # указывает, где разместить кнопку на экране. Второй
        #Кнопка  — это кнопка выхода, которая используется для закрытия графического интерфейса без
        # завершение викторины.
    def buttons(self):

        # Келесі сұраққа өтетін кнопка
        next_button = Button(gui, text="Келесі", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # кнопканы экранға шығару
        next_button.place(x=350, y=380)

        # Екінші кнопка программадан шығу үшін қажет
        quit_button = Button(gui, text="Аяқтау", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        # Программадан шығу кнопкасының орны
        quit_button.place(x=700, y=50)

    # Варианттарды экранғы шығару функциясы
    def display_options(self):
        val = 0

        # deselecting the options
        self.opt_selected.set(0)

        # перебор вариантов, которые будут отображаться для
        # текста переключателей.
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # Этот метод показывает текущий вопрос на экране
    def display_question(self):

        # настройка свойств вопроса
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')

        q_no.place(x=70, y=100)

    # Титл, шапканы орнатамыз
    def display_title(self):

        title = Label(gui, text="Тестілеу жүйесі",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        title.place(x=0, y=2)

    # Этот метод показывает переключатели для выбора вопроса на экране в указанной позиции.
    def radio_buttons(self):

        # инициализируйте список пустым списком вариантов
        q_list = []

        y_pos = 150

        # варианттарды 4-4 тен аламыз
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            # кнопкаларды массивке қосамыз
            q_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        return q_list


gui = Tk()

# размерін орнатамыз
gui.geometry("900x500")

gui.title("Тестілеу")

# gson форматтан ақпаратты аламыз
with open('data.json', encoding="utf-8") as f:
    data = json.load(f)

# оқылған файлдан сұрақтар мен жауаптарды бөлек айнмалыларғы сақтаймыз
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

# Quiz класының объектісін құрамыз
quiz = Quiz()

gui.mainloop()
