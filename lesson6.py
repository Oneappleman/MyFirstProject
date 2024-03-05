import requests
import sys
import tkinter
from PIL import Image
from io import BytesIO


app = tkinter.Tk()
x = "link Cat"
app.geometry("250x250")
label = tkinter.Label(app, text=x)
r = requests.get("https://api.thecatapi.com/v1/images/search")


if r.ok:
    answer = r.json()
    r_dict = dict(answer[0])
    for key, value in r_dict.items():
        print(f"{key} --- {value}")

def get_cat_button():
    global x
    x = key
    label.configure(text=x)

button = tkinter.Button(app, anchor="center", text ="Get a cat", command = get_cat_button)
app.mainloop()


