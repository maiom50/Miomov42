from app import app

#1
@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/info")
def info():
    return "This is an informational page."

#2
@app.route("/calc/<a>/<b>")
def calc(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        count = num1 + num2
        return f"The sum of {num1} and {num2} is {count}."
    except (ValueError, TypeError):
        return "Ошибка! Введите числа"

#3
@app.route("/reverse/<text>")
def reverse(text):
    flip_over = text[::-1]
    if len(flip_over) <= 1:
        return f"Длина слова должна привышать хотяб один символ"
    else:
        return f"{flip_over}"

#4
@app.route("/user/<name>/<int:age>")
def user(name, age):
    if age <= 0:
        return "Возраст не может быть быть меньше или равен 0"
    else:
        return f"Hello, {name}. You are {age} years old."