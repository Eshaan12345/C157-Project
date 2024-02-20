# Never ending Dice Game
from tkinter import *
from PIL import ImageTk, Image
'''Python image library is used to add images to ur platform'''
'''Image is used to open the image file'''
'''ImageTk is used to add the picture file to root window'''

root = Tk()
root.title('Endless Dice Game')
root.geometry("600x400")
root.configure(background = "IndianRed3")

img = ImageTk.PhotoImage(Image.open("Ball.png"))
charizard = ImageTk.PhotoImage(Image.open("charizard.jpg"))
bulbozor = ImageTk.PhotoImage(Image.open("bulbozor.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
shellder = ImageTk.PhotoImage(Image.open("shellder.png"))
grovyle = ImageTk.PhotoImage(Image.open("grovyle.jpg"))
flaaffy = ImageTk.PhotoImage(Image.open("flaaffy.jpg"))

player1 = Label(root, text = "Player 1", bg = "coral2", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = 'coral2', fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "SpringGreen2", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "SpringGreen2", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "VioletRed4", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn_player_1 = Button(root, image = img)
btn_player_1.place(relx = 0.2, rely = 0.7, anchor = CENTER)

btn_player_2 = Button(root, image = img)
btn_player_2.place(relx = 0.8, rely = 0.7, anchor = CENTER)

pokemons = ["Charizard", "Bulbasor", "Picachu", "Shellder", "Grovylle", "Flaaffy"]
pokemons_hp = [330, 200, 310, 70, 80, 90]

def select1():
    random_no = random.randint(0,5)
    pokemon = pokemons[random_no]
    score1 = pokemons_hp[random_no]
    player_1_score_label["text"] + score1
    
    if random_no == 0:
        random_dice_label["img"] = charizard
    if random_no == 1:
        random_dice_label["img"] = bulbozor
    if random_no == 2:
        random_dice_label["img"] = pikachu
    if random_no == 3:
        random_dice_label["img"] = shellder
    if random_no == 4:
        random_dice_label["img"] = grovyle
    if random_no == 5:
        random_dice_label["img"] = flaaffy
        
player1_btn = Button(root, img = img, command = select1)
player1_btn.place(relx = 0.2, rely = 0.8, anchor = CENTER)

def select2():
    random_no_2 = random.randint(0,5)
    pokemon_2 = pokemons[random_no]
    score2 = pokemons_hp[random_no]
    player_2_score_label["text"] + score1
    
    if random_no == 0:
        random_dice_label["img"] = charizard
    if random_no == 1:
        random_dice_label["img"] = bulbozor
    if random_no == 2:
        random_dice_label["img"] = pikachu
    if random_no == 3:
        random_dice_label["img"] = shellder
    if random_no == 4:
        random_dice_label["img"] = grovyle
    if random_no == 5:
        random_dice_label["img"] = flaaffy
        
player2_btn = Button(root, img = img, command = select2)
player2_btn.place(relx = 0.8, rely = 0.8, anchor = CENTER)
    

root.mainloop()