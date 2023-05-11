from tkinter import *
from parsing import *
import webbrowser

root = Tk()
root.title('в ананас')




# Доллар

dollar_label = Label (root, text="Kypс доллара: ", font=("Arial", 15)) 
dollar_label.grid(row=1, column=0, padx=10, pady=10)

#Евро
euro_label = Label (root, text="Kypc eвро: ", font=("Arial", 15))  
euro_label.grid(row=2, column=0, padx=10, pady=10)

#Рубль

ruble_label =  Label (root, text="Kурс рубля: ", font=("Arial", 15))

ruble_label.grid(row=3, column=0, padx=10, pady=10)

#TikTok

tiktok_label = Label (root, text="TikTok: ", font=("Arial", 15))

tiktok_label.grid(row=4, column=0, padx=10, pady=10)

#GitHub 
github_label = Label (root, text="GitHub: ", font=("Arial", 15))
github_label.grid(row=5, column=0, padx=10, pady=10)