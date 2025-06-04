from flask import Flask

# Создаем объект приложения Flask
app = Flask(__name__)

# Определяем маршрут и привязываем его к функции
@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/info")
def info():
    return "This is an informational page."

@app.route("/calc/<a>/<b>")
def calc(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        count = num1 + num2
        return f"The sum of {num1} and {num2} is {count}."
    except (ValueError, TypeError):
        return "Ошибка! Введите числа"

@app.route("/reverse/<text>")
def reverse(text):
    flip_over = text[::-1]
    if len(flip_over) <= 1:
        return f"Длина слова должна привышать хотяб один символ"
    else:
        return f"{flip_over}"

@app.route("/user/<name>/<int:age>")
def user(name, age):
    if age <= 0:
        return "Возраст не может быть быть меньше или равен 0"
    else:
        return f"Hello, {name}. You are {age} years old."


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)