import tkinter as tk
from parsing import *
import webbrowser

root = tk.Tk()
root.title("в ананас")


def App():

    def get_data():
        dollar = get_currency(DOLLAR_TENGE)
        euro = get_currency(EURO_TENGE)
        ruble = get_currency(RUBLE_TENGE)
        ALL_DATA = [dollar, euro, ruble]
        return ALL_DATA


    # Заголовок
    label = tk.Label(root, text="в ананас", font=("Arial", 20),
                     background="black", foreground="white", border=5)
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Доллар
    dollar_label = tk.Label(root, text="Курс доллара: ", font=("Arial", 15))
    dollar_label.grid(row=1, column=0, padx=10, pady=10)

    # Евро
    euro_label = tk.Label(root, text="Курс евро: ", font=("Arial", 15))
    euro_label.grid(row=2, column=0, padx=10, pady=10)

    # Рубль
    ruble_label = tk.Label(root, text="Курс рубля: ", font=("Arial", 15))
    ruble_label.grid(row=3, column=0, padx=10, pady=10)

    # TikTok
    tiktok_label = tk.Label(root, text="TikTok: ", font=("Arial", 15))
    tiktok_label.grid(row=4, column=0, padx=10, pady=10)


    def add_values(ALL_DATA):
        dollar_value = tk.Label(root, text=f"{ALL_DATA[0][0]} тг.", front=("Arial", 15))
        dollar_value.grid(row=1, column=1, padx=10, pady=10)
        euro_value = tk.Label(root, text=f"{ALL_DATA[1][0]} тг.", front=("Arial", 15))
        euro_value.grid(row=2, column=1, padx=10, pady=10)
        rulbe_value = tk.Label(root, text=f"{ALL_DATA[2][0]} тг.", front=("Arial", 15))
        rulbe_value.grid(row=3, column=1, padx=10, pady=10)
        tiktok_value = tk.Label(root, text=f"{ALL_DATA[3][0]} подписчиков", front=("Arial", 15))
        tiktok_value.grid(row=4, column=1, padx=10, pady=10)

    def destroy():
        dollar_value.destroy()
        euro_value.destroy()
        ruble_value.destroy()
        tiktok_value.destroy()

    def refresh():
        ALL_DATA = get_data()
        destroy_labels()
        add_values(ALL_DATA=ALL_DATA)
    
if __name__ == "__main__":
    App()
    root.mainloop()

