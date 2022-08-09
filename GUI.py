import tkinter as tk
from PIL import ImageTk, Image
import requests
import leagues
import teams

HEIGHT = 1400
WIDTH = 1500


def succc(entry1,entry2,entry3,entry4,entry5):
    url = "https://api-football-v1.p.rapidapi.com/v3/players"

    lg = leagues.league(entry1, entry2)
    print(lg)
    team = teams.team(entry4, lg)
    print(team)
    querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % entry3, "search": "%s" % entry5}

    headers = {
        "X-RapidAPI-Key": ,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.json())


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

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()

