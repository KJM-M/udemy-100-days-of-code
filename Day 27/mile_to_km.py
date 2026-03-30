from tkinter import *

font = ("Arial", 14)
one_mile_in_km = 1.60934


def convert_miles_to_km():
    miles = miles_input.get()
    try:
        kilometers = float(miles) * one_mile_in_km
        result_label.config(text=kilometers)

    except ValueError:
        result_label.config(text="Invalid Input")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(300, 200)
window.config(padx=50, pady=50)

miles_label = Label(text="Miles", font=font)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="=", font=font)
is_equal_label.grid(row=1, column=0)

kilometer_label = Label(text="Km", font=font)
kilometer_label.grid(row=1, column=2)

result_label = Label(text=0, font=font)
result_label.grid(row=1, column=1)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

button = Button(text="Calculate", font=font, command=convert_miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
