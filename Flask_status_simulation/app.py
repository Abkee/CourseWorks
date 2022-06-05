import random

from flask import Flask, render_template

app = Flask(__name__)


# Басты парақша
@app.route('/')
def hello_world():
    print(type(app))
    # массвты сандармен толтырамыз
    mas = prosec()
    # офлайн қолданушылар санын анықтаймыз
    of = mas.count(0)
    # онлайн қолданушылар саны
    on = mas.count(1)
    # бос емес қолданушылар
    za = mas.count(-1)
    p = 0
    # офлайн қолданушылар санына сәйкес, рандом уақытты қайтаратын функция
    tme = offtime(of)
    # Басты парақша html корсетеміз
    return render_template('index.html', mas=mas, of=of, on=on, za=za, tme=tme, p=p)

# колданушылар статусын рандом түрде шығаратын функция
# -1, 0, 1 аралыгындагы 100 саннан массивты кайтарады
def prosec():
    mas = [random.randint(-1, 1) for i in range(100)]
    return mas


#берілген қолданушылар санына сәйкес 1 мен 60 арасындағы сандар орналасқан массивты қайтарамыз
def offtime(n):
    mas = [random.randint(1, 60) for i in range(n)]
    return mas

# проектіні іске қосу
if __name__ == '__main__':
    app.run()
