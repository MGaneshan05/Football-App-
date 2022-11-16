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

switch = True


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

def picture4(info):
    url = info['response']['team']['logo']
    print(url)
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'tmimg{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
    z = 'tmimg.png'
    return z


def picture5(info):
    url = info['response']['league']['logo']
    print(url)
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
                                                                  height, weight, totalshots, ontrgt, gls, assists,
                                                                  totalpses, psacc, dribblswon, foulsdrawn, ycard,
                                                                  rcard, appearances, lineups, minutes, position)

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
                         '\nDuels Won: %s \nFouls Committed: %s' \
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
                                                                  height, weight, saves, conceeds,
                                                                  totalpses, psacc, ycard,
                                                                  rcard, appearances, lineups, minutes, position)

    except:
        basic_info = 'There was an error retrieving your data, please try again.'

    return basic_info


def tm1(entry1, entry2, entry3, entry4):
    try:
        if switch == False:
            x = "#26242f"

        else:
            x = "white"

        url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

        lg = leagues.league(entry1, entry2, entry3)
        print(lg)

        team = teams.team(entry4, lg, entry3)
        print(team)

        querystring = {"league": "%s" % lg, "season": "%s" % entry3, "team": "%s" % team}

        headers = {
            "X-RapidAPI-Key": "bf52d49e93msh937c0f1742ea513p1b23c2jsnfcd110a9c315",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        info = response.json()
        print(info)

        json_object = json.dumps(info, indent=4)
        with open("team_info.json", "w") as outfile:
            outfile.write(json_object)
        q = picture4(info)
        o = picture5(info)

        img1 = ImageTk.PhotoImage(Image.open('tmimg.png'))
        img1_label = tk.Label(root, image=img1, bg=x)
        img1_label.photo = img1
        img1_label.place(relx=0.13, rely=0.36, relwidth=0.1, relheight=0.18)
        img2 = ImageTk.PhotoImage(Image.open('lgimg.png'))
        img2_label = tk.Label(root, image=img2, bg=x)
        img2_label.photo = img2
        img2_label.place(relx=0.13, rely=0.56, relwidth=0.1, relheight=0.15)
        label1['text'] = format_response(info)

        def clear():
            label1.config(text='')
            img1_label.config(image='')
            img2_label.config(image='')
            img3_label.config(image='')

        button3 = tk.Button(upper_frame, text='Clear Slot 1', font=('Trebuchet MS', 15), command=lambda: clear())

        button3.place(relx=0.7, rely=0.6, relwidth=0.15, relheight=0.4)
    except:
        print('sad')
        label1.config(text='There was an error processing \nyour request.'
                           '\nPlease check your spelling \nand try again.')

    return info


def ent1(entry1, entry2, entry3, entry4, entry5):
    try:
        if switch == False:
            x = "#26242f"

        else:
            x = "white"

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
            img1_label = tk.Label(root, image=img1, bg=x)
            img1_label.photo = img1
            img1_label.place(relx=0.13, rely=0.36, relwidth=0.1, relheight=0.18)
            img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
            img2_label = tk.Label(root, image=img2, bg=x)
            img2_label.photo = img2
            img2_label.place(relx=0.13, rely=0.56, relwidth=0.1, relheight=0.15)
            img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
            img3_label = tk.Label(root, image=img3, bg=x)
            img3_label.photo = img3
            img3_label.place(relx=0.13, rely=0.7, relwidth=0.1, relheight=0.2)
            label1['text'] = format_response(info)

            def clear():
                label1.config(text='')
                img1_label.config(image='')
                img2_label.config(image='')
                img3_label.config(image='')

            button3 = tk.Button(upper_frame, text='Clear Slot 1', font=('Trebuchet MS', 15), command=lambda: clear())

            button3.place(relx=0.7, rely=0.6, relwidth=0.15, relheight=0.4)


        else:
            url = "https://api-football-v1.p.rapidapi.com/v3/players"

            lg = leagues.league(entry1, entry2, entry3)
            print(lg)

            team = teams.team(entry4, lg, entry3)

            print(team)

            querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % entry3, "search": "%s" % entry5}

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
            img1_label = tk.Label(root, image=img1, bg=x)
            img1_label.photo = img1
            img1_label.place(relx=0.13, rely=0.36, relwidth=0.1, relheight=0.18)
            img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
            img2_label = tk.Label(root, image=img2, bg=x)
            img2_label.photo = img2
            img2_label.place(relx=0.13, rely=0.56, relwidth=0.1, relheight=0.15)
            img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
            img3_label = tk.Label(root, image=img3, bg=x)
            img3_label.photo = img3
            img3_label.place(relx=0.13, rely=0.7, relwidth=0.1, relheight=0.2)
            label1['text'] = format_response(info)

            def clear():
                label1.config(text='')
                img1_label.config(image='')
                img2_label.config(image='')
                img3_label.config(image='')

            button3 = tk.Button(upper_frame, text='Clear Slot 1', font=('Trebuchet MS', 15), command=lambda: clear())

            button3.place(relx=0.7, rely=0.6, relwidth=0.15, relheight=0.4)
    except:
        print('sad')
        label1.config(text='There was an error processing \nyour request.'
                           '\nPlease check your spelling \nand try again.')

    return info


def ent2(entry1, entry2, entry3, entry4, entry5):
    try:
        if switch == False:
            x = "#26242f"

        else:
            x = "white"

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
            img1_label = tk.Label(root, image=img1, bg=x)
            img1_label.photo = img1
            img1_label.place(relx=0.4, rely=0.36, relwidth=0.1, relheight=0.18)
            img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
            img2_label = tk.Label(root, image=img2, bg=x)
            img2_label.photo = img2
            img2_label.place(relx=0.4, rely=0.56, relwidth=0.1, relheight=0.15)
            img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
            img3_label = tk.Label(root, image=img3, bg=x)
            img3_label.photo = img3
            img3_label.place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.2)
            label2['text'] = format_response(info)

            def clear():
                label2.config(text='')
                img1_label.config(image='')
                img2_label.config(image='')
                img3_label.config(image='')

            button4 = tk.Button(upper_frame, text='Clear Slot 2', font=('Trebuchet MS', 15), command=lambda: clear())

            button4.place(relx=0.85, rely=0.6, relwidth=0.15, relheight=0.4)


        else:
            url = "https://api-football-v1.p.rapidapi.com/v3/players"

            lg = leagues.league(entry1, entry2, entry3)
            print(lg)

            team = teams.team(entry4, lg, entry3)

            print(team)

            querystring = {"team": "%s" % team, "league": "%s" % lg, "season": "%s" % entry3, "search": "%s" % entry5}

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
            img1_label = tk.Label(root, image=img1, bg=x)
            img1_label.photo = img1
            img1_label.place(relx=0.4, rely=0.36, relwidth=0.1, relheight=0.18)
            img2 = ImageTk.PhotoImage(Image.open('tmimg.png'))
            img2_label = tk.Label(root, image=img2, bg=x)
            img2_label.photo = img2
            img2_label.place(relx=0.4, rely=0.56, relwidth=0.1, relheight=0.15)
            img3 = ImageTk.PhotoImage(Image.open('lgimg.png'))
            img3_label = tk.Label(root, image=img3, bg=x)
            img3_label.photo = img3
            img3_label.place(relx=0.4, rely=0.7, relwidth=0.1, relheight=0.2)
            label2['text'] = format_response(info)

            def clear():
                label2.config(text='')
                img1_label.config(image='')
                img2_label.config(image='')
                img3_label.config(image='')

            button4 = tk.Button(upper_frame, text='Clear Slot 2', font=('Trebuchet MS', 15), command=lambda: clear())

            button4.place(relx=0.85, rely=0.6, relwidth=0.15, relheight=0.4)
    except:
        print('sad')
        label2.config(text='There was an error processing \nyour request.'
                           '\nPlease check your spelling \nand try again.')
    return info


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image1 = ImageTk.PhotoImage(Image.open('1.jpg'))
background_image2 = ImageTk.PhotoImage(Image.open('2.jpg'))
background_label = tk.Label(root, image=background_image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='sky blue', bd=5)
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.25, anchor='n')

entry1 = tk.Entry(upper_frame, font=('Trebuchet MS', 15), fg='black')
entry1.place(relx=0.5, rely=0, relwidth=0.35, relheight=0.2)

entry2 = tk.Entry(upper_frame, font=('Trebuchet MS', 15), fg='black')
entry2.place(relx=0.5, rely=0.2, relwidth=0.35, relheight=0.2)

entry3 = tk.Entry(upper_frame, font=('Trebuchet MS', 15), fg='black')
entry3.place(relx=0.5, rely=0.4, relwidth=0.35, relheight=0.2)

entry4 = tk.Entry(upper_frame, font=('Trebuchet MS', 15), fg='black')
entry4.place(relx=0.5, rely=0.6, relwidth=0.35, relheight=0.2)

entry5 = tk.Entry(upper_frame, font=('Trebuchet MS', 15), fg='black')
entry5.place(relx=0.5, rely=0.8, relwidth=0.35, relheight=0.2)

label8 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Country', fg='black')
label8.place(relx=0.325, rely=0, relwidth=0.175, relheight=0.2)

label3 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='League', fg='black')
label3.place(relx=0.325, rely=0.2, relwidth=0.175, relheight=0.2)

label4 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Season', fg='black')
label4.place(relx=0.325, rely=0.4, relwidth=0.175, relheight=0.2)

label5 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Team', fg='black')
label5.place(relx=0.325, rely=0.6, relwidth=0.175, relheight=0.2)

label6 = tk.Label(upper_frame, font=('Trebuchet MS', 15), bg='white', text='Player', fg='black')
label6.place(relx=0.325, rely=0.8, relwidth=0.175, relheight=0.2)

label7 = tk.Label(upper_frame, font=('Trebuchet MS', 11), bg='white', justify='left'
                  ,
                  text='Welcome to PlayerFinder 2022! \n To Start, fill in the details for your desired player. In the name section, \n please type only the players very last name,'
                       'for example "Trent Alexander \n Arnold", you would type Arnold. You have two slots available, Search \n and Compare. Search will fill the first slot'
                       ', and compare will fill the \n second. After every search, make sure to clear both slots. \n Please select dark or light mode before using the app.',
                  anchor='nw', fg='black')

label7.place(relx=0, relwidth=0.35, relheight=1)

button1 = tk.Button(upper_frame, text="Search!", font=('Trebuchet MS', 15), command=lambda: ent1(entry1.get(),
                                                                                                 entry2.get(),
                                                                                                 entry3.get(),
                                                                                                 entry4.get(),
                                                                                                 entry5.get()))
button1.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.3)

button2 = tk.Button(upper_frame, text="Compare!", font=('Trebuchet MS', 15), command=lambda: ent2(entry1.get(),
                                                                                                  entry2.get(),
                                                                                                  entry3.get(),
                                                                                                  entry4.get(),
                                                                                                  entry5.get()))
button2.place(relx=0.7, rely=0.3, relwidth=0.3, relheight=0.3)

lower_frame = tk.Frame(root, bg='sky blue', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='white', font=('Trebuchet MS', 15), justify='left', bd=4)
label.place(relwidth=1, relheight=1)

label1 = tk.Label(lower_frame, bg='white', font=('Trebuchet MS', 15), anchor='nw', justify='left', bd=4)
label1.place(relx=0.14, rely=0, relwidth=0.4, relheight=1)

label2 = tk.Label(lower_frame, bg='white', font=('Trebuchet MS', 15), anchor='nw', justify='left', bd=4)
label2.place(relx=0.5, rely=0, relwidth=0.4, relheight=1)

img1_label = tk.Label(root, bg='white')
img1_label.place(x=750, y=390, relwidth=0.1, relheight=0.18)

img2_label = tk.Label(root, bg='white')
img2_label.place(x=750, y=560, relwidth=0.1, relheight=0.15)

img3_label = tk.Label(root, bg='white')
img3_label.place(x=750, y=720, relwidth=0.1, relheight=0.2)

button3 = tk.Button(upper_frame, text='Clear Slot 1', font=('Trebuchet MS', 15))

button3.place(relx=0.7, rely=0.6, relwidth=0.15, relheight=0.4)

button4 = tk.Button(upper_frame, text='Clear Slot 2', font=('Trebuchet MS', 15))

button4.place(relx=0.85, rely=0.6, relwidth=0.15, relheight=0.4)


def toggle():
    global switch
    if switch == True:
        background_label.config(image=background_image2)
        label.config(bg="#26242f", fg='white')
        label1.config(bg="#26242f", fg='white')
        label2.config(bg="#26242f", fg='white')
        label3.config(bg="#26242f", fg='white')
        label4.config(bg="#26242f", fg='white')
        label5.config(bg="#26242f", fg='white')
        label6.config(bg="#26242f", fg='white')
        label7.config(bg="#26242f", fg='white')
        entry1.config(bg="#26242f", fg='white')
        entry2.config(bg="#26242f", fg='white')
        entry3.config(bg="#26242f", fg='white')
        entry4.config(bg="#26242f", fg='white')
        entry5.config(bg="#26242f", fg='white')
        label8.config(bg="#26242f", fg='white')
        lower_frame.config(bg='beige')
        upper_frame.config(bg='beige')
        button5.config(text='Light Mode', fg='white', bg="#26242f",
                       activebackground="#26242f")
        img1_label.config(bg="#26242f")
        img2_label.config(bg="#26242f")
        img3_label.config(bg="#26242f")
        switch = False
        print('p')
    else:
        background_label.config(image=background_image1)
        label.config(bg="white", fg='black')
        label1.config(bg="white", fg='black')
        label2.config(bg="white", fg='black')
        label3.config(bg="white", fg='black')
        label4.config(bg="white", fg='black')
        label5.config(bg="white", fg='black')
        label6.config(bg="white", fg='black')
        label7.config(bg="white", fg='black')
        entry1.config(bg="white", fg='black')
        entry2.config(bg="white", fg='black')
        entry3.config(bg="white", fg='black')
        entry4.config(bg="white", fg='black')
        entry5.config(bg="white", fg='black')
        label8.config(bg="white", fg='black')
        lower_frame.config(bg='sky blue')
        upper_frame.config(bg='sky blue')
        button5.config(text='Dark Mode', fg='black', bg="white",
                       activebackground="white")
        img1_label.config(bg="white")
        img2_label.config(bg="white")
        img3_label.config(bg="white")
        switch = True
        print('q')


button5 = tk.Button(upper_frame, bd=0, bg="white", activebackground="white", command=toggle, text='Dark Mode')

button5.place(relx=0, rely=0.7, relwidth=0.3, relheight=0.25)

button6 = tk.Button(upper_frame, bd=0, text='Team View Slot 1', command=lambda: tm1(entry1.get(),
                                                                                    entry2.get(), entry3.get(),
                                                                                    entry4.get(), ))
button6.place(relx=0, rely=0.6, relwidth=0.1, relheight=0.1)
button7 = tk.Button(upper_frame, bd=0, text='Team View Slot 2')
button7.place(relx=0, rely=0.7, relwidth=0.1, relheight=0.1)

root.mainloop()
