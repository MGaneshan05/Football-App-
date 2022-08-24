import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import requests
import json
import leagues
import teams
import os

HEIGHT = 1080
WIDTH = 1920



def picture1(info):
    url = info['response'][0]['player']['photo']
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'plyrimg{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    z = 'plyrimg.png'
    return z


def picture2(info):
    url = info['response'][0]['statistics'][0]['team']['logo']
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'tmimg{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    z = 'tmimg.png'
    return z


def picture3(info):
    url = info['response'][0]['statistics'][0]['league']['logo']
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'lgimg{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    z = 'lgimg.png'
    return z


def format_response(info):
    try:
        first_name = info['response'][0]['player']['firstname']
        last_name = info['response'][0]['player']['lastname']
        age = info['response'][0]['player']['age']
        birth = info['response'][0]['player']['birth']['date']
        nationality = info['response'][0]['player']['nationality']
        height = info['response'][0]['player']['height']
        weight = info['response'][0]['player']['weight']
        appearances = info['response'][0]['statistics'][0]['games']['appearences']
        lineups = info['response'][0]['statistics'][0]['games']['lineups']
        minutes = info['response'][0]['statistics'][0]['games']['minutes']
        position = info['response'][0]['statistics'][0]['games']['position']
        totalshots = info['response'][0]['statistics'][0]['shots']['total']
        ontrgt = info['response'][0]['statistics'][0]['shots']['on']
        gls = info['response'][0]['statistics'][0]['goals']['total']
        conceeds = info['response'][0]['statistics'][0]['goals']['conceded']
        assists = info['response'][0]['statistics'][0]['goals']['assists']
        saves = info['response'][0]['statistics'][0]['goals']['saves']
        totalpses = info['response'][0]['statistics'][0]['passes']['total']
        keypses = info['response'][0]['statistics'][0]['passes']['key']
        psacc = info['response'][0]['statistics'][0]['passes']['accuracy']
        tckles = info['response'][0]['statistics'][0]['tackles']['total']
        blocks = info['response'][0]['statistics'][0]['tackles']['blocks']
        intrcpt = info['response'][0]['statistics'][0]['tackles']['interceptions']
        ttlduels = info['response'][0]['statistics'][0]['duels']['total']
        wonduels = info['response'][0]['statistics'][0]['duels']['won']
        drbblsttl = info['response'][0]['statistics'][0]['dribbles']['attempts']
        dribblswon = info['response'][0]['statistics'][0]['dribbles']['success']
        foulsdrawn = info['response'][0]['statistics'][0]['fouls']['drawn']
        foulscom = info['response'][0]['statistics'][0]['fouls']['committed']
        ycard = info['response'][0]['statistics'][0]['cards']['yellow']
        rcard = info['response'][0]['statistics'][0]['cards']['red']

        if info['response'][0]['statistics'][0]['games']['position'] == 'Attacker':
            basic_info = 'First Name: %s  \nLast Name: %s  \nAge: %s  \nBirthday: %s  \nNationality: %s  \nHeight: %s' \
                     '\nWeight: %s \nTotal Shots: %s On target: %s \nGoals: %s \nAssists: %s \nTotal Passes: %s ' \
                            '\nPass Accuracy: %s \nSuccessful Dribbles: %s \nFouls Drawn: %s ' \
                             '\nYellow cards: %s Red cards: %s \nAppearances: %s \nStarts: %s ' \
                            '\nMinutes Played: %s \nPosition: %s' % (first_name, last_name, age, birth, nationality,
                                                                     height,weight, totalshots, ontrgt, gls, assists,
                                                                     totalpses, psacc, dribblswon, foulsdrawn, ycard,
                                                                     rcard, appearances,lineups, minutes, position)

        if info['response'][0]['statistics'][0]['games']['position'] == 'Midfielder':
            basic_info = 'First Name: %s  \nLast Name: %s  \nAge: %s  \nBirthday: %s  \nNationality: %s  \nHeight: %s  ' \
                         '\nWeight: %s \nTotal Shots: %s On target: %s \nGoals: %s \nAssists: %s \nTotal Passes: %s ' \
                         '\nKey Passes: %s \nPass Accuracy: %s \nSuccessful Dribbles: %s \nTackles: %s' \
                         '\nInterceptions: %s \nDuels Won: \nFouls Drawn: %s ' \
                         '\nYellow cards: %s Red cards: %s \nAppearances: %s \nStarts: %s ' \
                         '\nMinutes Played: %s \nPosition: %s' % (first_name, last_name, age, birth, nationality,
                                                                  height, weight, totalshots, ontrgt, gls, assists,
                                                                  totalpses, psacc, dribblswon, tckles, intrcpt,
                                                                  wonduels, foulsdrawn, ycard, rcard,
                                                                  appearances, lineups, minutes, position)

        if info['response'][0]['statistics'][0]['games']['position'] == 'Defender':
            basic_info = 'First Name: %s  \nLast Name: %s  \nAge: %s  \nBirthday: %s  \nNationality: %s  \nHeight: %s' \
                     '\nWeight: %s \nConceded: %s \nGoals: %s \nAssists: %s \nTotal Passes: %s ' \
                            '\nPass Accuracy: %s \nSuccessful Dribbles: %s \nTackles: %s \nBlocks: %s ' \
                         '\nDuels Won: %s \nFouls Committed: %s'  \
                             '\nYellow cards: %s Red cards: %s \nAppearances: %s \nStarts: %s ' \
                            '\nMinutes Played: %s \nPosition: %s' % (first_name, last_name, age, birth, nationality,
                                                                     height, weight, conceeds, gls, assists,
                                                                     totalpses, psacc, dribblswon, tckles, blocks,
                                                                     wonduels, foulscom, ycard,
                                                                     rcard, appearances, lineups, minutes, position)
        if info['response'][0]['statistics'][0]['games']['position'] == 'Goalkeeper':
            basic_info = 'First Name: %s  \nLast Name: %s  \nAge: %s  \nBirthday: %s  \nNationality: %s  \nHeight: %s' \
                         '\nWeight: %s \nSaves: %s \nConceded: %s \nTotal Passes: %s ' \
                         '\nPass Accuracy: %s ' \
                         '\nYellow cards: %s Red cards: %s \nAppearances: %s \nStarts: %s ' \
                         '\nMinutes Played: %s \nPosition: %s' % (first_name, last_name, age, birth, nationality,
                                                                  height, weight,saves, conceeds,
                                                                  totalpses, psacc, ycard,
                                                                  rcard, appearances, lineups, minutes, position)

    except:
        basic_info = 'There was an error retrieving your data, please try again.'

    return basic_info

def ent1(entry1,entry2,entry3,entry4,entry5):
    if entry5 == 'Son':

        url = "https://api-football-v1.p.rapidapi.com/v3/players"

        lg = leagues.league(entry1, entry2, entry3)
        print(lg)

        team = teams.team(entry4, lg, entry3)

        print(team)

        querystring = {"id": "186", "league": "%s" % lg, "season": "%s" % entry3}

        headers = {
            "X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        info = response.json()

        q = picture1(info)
        o = picture2(info)
        j = picture3(info)

        json_object = json.dumps(info, indent=4)

        # Writing to sample.json

        with open("user_info.json", "w") as outfile:
            outfile.write(json_object)

        img1 = ImageTk.PhotoImage(Image.open('plyrimg.png'))
        img1_label = tk.Label(root, image=img1, bg='white')
        img1_label.photo = img1
        img1_label.place(x=250, y=390, relwidth=0.1, relheight=0.15)
        img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
        img2_label = tk.Label(root, image=img2, bg='white')
        img2_label.photo = img2
        img2_label.place(x=250, y=560, relwidth=0.1, relheight=0.15)
        img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
        img3_label = tk.Label(root, image=img3, bg='white')
        img3_label.photo = img3
        img3_label.place(x=250, y=720, relwidth=0.1, relheight=0.2)
        label1['text'] = format_response(info)




    else:
        url = "https://api-football-v1.p.rapidapi.com/v3/players"

        lg = leagues.league(entry1, entry2, entry3)
        print(lg)

        team = teams.team(entry4, lg, entry3)

        print(team)

        querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % entry3, "search": "%s" % entry5}

        headers = {
        "X-RapidAPI-Key":"bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315" ,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        info = response.json()

        q = picture1(info)
        o = picture2(info)
        j = picture3(info)

        json_object = json.dumps(info, indent=4)

        # Writing to sample.json

        with open("user_info.json", "w") as outfile:
            outfile.write(json_object)

        img1 = ImageTk.PhotoImage(Image.open('plyrimg.png'))
        img1_label = tk.Label(root, image=img1, bg="white")
        img1_label.photo = img1
        img1_label.place(x=250, y=390, relwidth=0.1, relheight=0.15)
        img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
        img2_label = tk.Label(root, image=img2, bg="white")
        img2_label.photo = img2
        img2_label.place(x=250, y=560, relwidth=0.1, relheight=0.15)
        img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
        img3_label = tk.Label(root, image=img3, bg="white")
        img3_label.photo = img3
        img3_label.place(x=250, y=720, relwidth=0.1, relheight=0.2)
        label1['text'] = format_response(info)

    return info


def ent2(entry1,entry2,entry3,entry4,entry5):

    if entry5 == 'Son':

        url = "https://api-football-v1.p.rapidapi.com/v3/players"

        lg = leagues.league(entry1, entry2, entry3)
        print(lg)

        team = teams.team(entry4, lg, entry3)

        print(team)

        querystring = {"id": "186", "league": "%s" % lg, "season": "%s" % entry3}

        headers = {
            "X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        info = response.json()

        q = picture1(info)
        o = picture2(info)
        j = picture3(info)

        json_object = json.dumps(info, indent=4)

        # Writing to sample.json

        with open("user_info2.json", "w") as outfile:
            outfile.write(json_object)

        img1 = ImageTk.PhotoImage(Image.open('plyrimg.png'))
        img1_label = tk.Label(root, image=img1, bg='white')
        img1_label.photo = img1
        img1_label.place(x=750, y=390, relwidth=0.1, relheight=0.15)
        img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
        img2_label = tk.Label(root, image=img2, bg='white')
        img2_label.photo = img2
        img2_label.place(x=750, y=560, relwidth=0.1, relheight=0.15)
        img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
        img3_label = tk.Label(root, image=img3, bg='white')
        img3_label.photo = img3
        img3_label.place(x=750, y=720, relwidth=0.1, relheight=0.2)
        label2['text'] = format_response(info)




    else:
        url = "https://api-football-v1.p.rapidapi.com/v3/players"

        lg = leagues.league(entry1, entry2, entry3)
        print(lg)

        team = teams.team(entry4, lg, entry3)

        print(team)

        querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % entry3, "search": "%s" % entry5}

        headers = {
        "X-RapidAPI-Key":"bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315" ,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        info = response.json()

        q = picture1(info)
        o = picture2(info)
        j = picture3(info)

        json_object = json.dumps(info, indent=4)

        # Writing to sample.json

        with open("user_info2.json", "w") as outfile:
            outfile.write(json_object)

        img1 = ImageTk.PhotoImage(Image.open('plyrimg.png'))
        img1_label = tk.Label(root, image=img1, bg='white')
        img1_label.photo = img1
        img1_label.place(x=750, y=390, relwidth=0.1, relheight=0.15)
        img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
        img2_label = tk.Label(root, image=img2, bg='white')
        img2_label.photo = img2
        img2_label.place(x=750, y=560, relwidth=0.1, relheight=0.15)
        img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
        img3_label = tk.Label(root, image=img3, bg='white')
        img3_label.photo = img3
        img3_label.place(x=750, y=720, relwidth=0.1, relheight=0.2)
        label2['text'] = format_response(info)

    return info


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image1 = ImageTk.PhotoImage(Image.open('1.jpg'))
background_image2 = ImageTk.PhotoImage(Image.open('2.jpg'))
background_label = tk.Label(root, image=background_image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

upper_frame = tk.Frame(root,bg='sky blue', bd=5)
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.25, anchor='n')

entry1 = tk.Entry(upper_frame, font=('Trebuchet MS', 15))
entry1.place(relx=0.5, rely=0, relwidth=0.35, relheight=0.2)

entry2 = tk.Entry(upper_frame, font=('Trebuchet MS', 15))
entry2.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.2)

entry3 = tk.Entry(upper_frame, font=('Trebuchet MS', 15))
entry3.place(relx=0.5, rely=0.4, relwidth=0.35, relheight=0.2)

entry4 = tk.Entry(upper_frame, font=('Trebuchet MS', 15))
entry4.place(relx=0.5, rely=0.6, relwidth=0.35, relheight=0.2)

entry5 = tk.Entry(upper_frame, font=('Trebuchet MS', 15))
entry5.place(relx=0.5, rely=0.8, relwidth=0.35, relheight=0.2)

label8 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Country')
label8.place(relx=0.325, rely=0, relwidth=0.175, relheight=0.2)

label3 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='League')
label3.place(relx=0.325, rely=0.2, relwidth=0.175, relheight=0.2)

label4 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Season')
label4.place(relx=0.325, rely=0.4, relwidth=0.175, relheight=0.2)

label5 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Team')
label5.place(relx=0.325, rely=0.6, relwidth=0.175, relheight=0.2)

label6 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Player')
label6.place(relx=0.325, rely=0.8, relwidth=0.175, relheight=0.2)

label7 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', justify='left'
                  , text='Welcome to PlayerFinder 2022! \n(Some instructional text)', anchor='nw')

label7.place(relx=0, relwidth=0.35, relheight=1)

button1 = tk.Button(upper_frame, text="Search!",  font=('Trebuchet MS', 15), command=lambda: ent1(entry1.get(),
                                                                                    entry2.get(), entry3.get(),
                                                                                    entry4.get(), entry5.get()))
button1.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.5)

button2 = tk.Button(upper_frame, text="Compare!",  font=('Trebuchet MS', 15), command=lambda: ent2(entry1.get(),
                                                                                    entry2.get(), entry3.get(),
                                                                                    entry4.get(), entry5.get()))
button2.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.5)

lower_frame = tk.Frame(root,bg='sky blue', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', font=('Trebuchet MS', 15), justify='left', bd=4)
label.place(relwidth=1, relheight=1)

label1 = tk.Label(lower_frame, bg='white', font=('Trebuchet MS', 15), anchor='nw', justify='left', bd=4)
label1.place(relx=0.14, rely=0, relwidth=0.4, relheight=1)

label2 = tk.Label(lower_frame, bg='white', font=('Trebuchet MS', 15), anchor='nw', justify='left', bd=4)
label2.place(relx=0.5, rely=0, relwidth=0.4, relheight=1)

switch = True
def toggle():

    global switch
    if switch == True:
        button3.config(bg="#26242f",
                      activebackground="#26242f")
        background_label.config(image=background_image2)
        label.config(bg="#26242f")
        label1.config(bg="#26242f")
        label2.config(bg="#26242f")
        label3.config(bg="#26242f")
        label4.config(bg="#26242f")
        label5.config(bg="#26242f")
        label6.config(bg="#26242f")
        label7.config(bg="#26242f")
        entry1.config(bg="#26242f")
        entry2.config(bg="#26242f")
        entry3.config(bg="#26242f")
        entry4.config(bg="#26242f")
        entry5.config(bg="#26242f")
        label8.config(bg="#26242f")
        lower_frame.config(bg="#26242f")
        switch = False
        print('p')
    else:
        button3.config(bg="white",
                      activebackground="white")
        background_label.config(image=background_image1)
        # Changes the window to light theme
        switch= True
        print('q')

button3 = tk.Button(upper_frame,
                bd=0, bg="white",
                activebackground="white",
                command=toggle,
                    text = 'read this!')

button3.place(relx=0, rely=0.5, relwidth=0.3, relheight=0.25)

root.mainloop()

