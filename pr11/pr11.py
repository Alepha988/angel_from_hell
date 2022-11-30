import requests
from tkinter import *


def click():
    username = txt.get()
    repositoriy = txt.get()
    r = requests.get(f'https://api.github.com/repos/{username}/{repositoriy}').json()
    with open('C:\\Users\\Aleph\\PycharmProjects\\pythonProject15\\pr11', 'a+') as f:
        if 'company' in r:
            f.write(f"'company': '{r['company']}\n")
        else:
            f.write("'company: None'\n")
        if 'created_at' in r:
            f.write(f"'created_at': '{r['created_at']}\n")
        else:
            f.write("'None'\n")
        if 'email' in r:
            f.write(f"'email': '{r['email']}\n")
        else:
            f.write("'email: None'\n")
        if 'id' in r:
            f.write(f"'id': '{r['id']}\n")
        else:
            f.write('None')
        if 'name' in r:
            f.write(f"'name': '{r['name']}\n")
        else:
            f.write('None')
        if 'url' in r:
            f.write(f"'url': '{r['url']}\n")
        else:
            f.write('None')

window = Tk()
window.title('Aleksey Morgunov')
window.geometry('600x300')
lbl = Label(window, text='Введите репозиторий', font=('Times New Roman', 20))
lbl.grid(column=0, row=0)
btn = Button(window, text='Подтвердить', command=click)
btn.grid(column=2, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
window.mainloop()
