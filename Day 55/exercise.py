from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="color:green; text-align:center">Hello, World!</h1>'
            '<p style="text-align:center;">paragraph</p>'
            '<img "src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTR2dXAxcjhuZmM4aTNvdmVsa3dzcWowazF2ZjJ4MXRidjd2NjR2cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif">')



@app.route("/bye")
def bye():
    return "Bye!"


#Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def hello_name(name, number):
    return f"Hello there {name}, you are {number} years old!"



def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)