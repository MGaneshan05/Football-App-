import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import requests
import json
import leagues
import teams
import os

HEIGHT = 1400
WIDTH = 1500


def picture(info):
    url = info['response'][0]['player']['photo']
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'plyrimg{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    z = 'plyrimg.png'
    return z


def format_response(info):
    try:
        first_name = info['response'][0]['player']['firstname']
        last_name = info['response'][0]['player']['lastname']
        age = info['response'][0]['player']['age']
        birth = info['response'][0]['player']['birth']
        nationality = info['response'][0]['player']['nationality']
        height = info['response'][0]['player']['height']
        weight = info['response'][0]['player']['weight']
        basic_info = 'First Name: %s  \nLast Name: %s  \nAge: %s  \nBirthday: %s  \nNationality: %s  \nHeight: %s  ' \
                     '\nWeight: %s' % (first_name, last_name, age, birth, nationality, height, weight)

    except:
        basic_info = 'There was an error retrieving your data, please try again.'

    return basic_info


def succc(entry1,entry2,entry3,entry4,entry5):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"

    lg = leagues.league(entry1, entry2)
    print(lg)
    team = teams.team(entry4, lg)
    print(team)
    querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % entry3, "search": "%s" % entry5}

    headers = {
        "X-RapidAPI-Key":"bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315" ,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    info = response.json()
    q = picture(info)
    json_object = json.dumps(info, indent=4)

    # Writing to sample.json
    with open("user_info.json", "w") as outfile:
        outfile.write(json_object)

    label['text'] = format_response(info)
    label['image'] = q


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('pitch.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='light blue',bd=5)
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.25, anchor='n')

entry1 = tk.Entry(upper_frame, font=4)
entry1.place(rely=0, relwidth=0.7, relheight=0.2)

entry2 = tk.Entry(upper_frame, font=4)
entry2.place(rely=0.2, relwidth=0.7, relheight=0.2)

entry3 = tk.Entry(upper_frame, font=4)
entry3.place(rely=0.4, relwidth=0.7, relheight=0.2)

entry4 = tk.Entry(upper_frame, font=4)
entry4.place(rely=0.6, relwidth=0.7, relheight=0.2)

entry5 = tk.Entry(upper_frame, font=4)
entry5.place(rely=0.8, relwidth=0.7, relheight=0.2)

button1 = tk.Button(upper_frame, text="Search!", font=40, command=lambda: succc(entry1.get(),
                                                                                    entry2.get(), entry3.get(),
                                                                                    entry4.get(), entry5.get()))
button1.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Times New Roman', 15), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()

