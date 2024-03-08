import requests
import tkinter
from PIL import Image, ImageTk
from io import BytesIO

app = tkinter.Tk()
x = "link Cat"
app.geometry("1920x1080")
label = tkinter.Label(app, text='Place of image')
label_link = tkinter.Label(app, text="Cat's link")
def update():
    global r
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.ok:
        answer = r.json()
        global r_dict
        r_dict = dict(answer[0])
        for key, value in r_dict.items():
            # print(f"{key} --- {value}")
            if key == 'url':
                global link
                link = value
            else:
                pass

        global cat
        cat = requests.get(r_dict['url'])
        global cat_image
        cat_image = Image.open(BytesIO(cat.content))
        global cat_image_content
        cat_image_content = ImageTk.PhotoImage(cat_image)
        label_link.config(text=link)


def get_cat_button():
    label.config(image=cat_image_content, text='')
    label_link.config(text=link)


button = tkinter.Button(app, anchor="center", text ="Get a cat", command = get_cat_button)
button_update = tkinter.Button(app, anchor="nw", text ="Update a cat", command = update)
label.pack()
label.grid(column=3, row=2)
button.grid(column=1,row=0)
button_update.grid(column=1, row=1)
label_link.grid(column=2,row=0)

app.mainloop()


