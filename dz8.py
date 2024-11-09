import requests
import tkinter as tk
from tkinter import messagebox


# Клас для конвертації валют
class dd:
    def __init__(self, ss, sd):
        self.ss = ss
        self.sd = sd

    def tusd(self, amount):
        return amount / self.sd



def efn():
    try:
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        if response.status_code == 200:
            data = response.json()

            for dsd in data:
                if dsd['cc'] == 'USD':
                    return dsd['rate']
            raise Exception("Error")
        else:
            raise Exception("Error")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None



def convert():
    try:
        ua = float(entry_ua.get())
        if ua <= 0:
            raise ValueError("Zero Error")

        sd = efn()
        if sd is None:
            return

        converter = dd(ss="UAH", sd=sd)
        usd = converter.tusd(ua)

        result_label.config(text=f"Долар США: {usd:.2f} USD")

    except ValueError as e1:
        messagebox.showerror("Error", f"Error: {e1}")
    except Exception as e:
        messagebox.showerror("Error", str(e))



root = tk.Tk()
root.title("Converter")
root.geometry("400x300")


label_ua = tk.Label(root, text="Введіть кількість гривень:")
label_ua.pack(pady=10)

entry_ua = tk.Entry(root)
entry_ua.pack(pady=10)


convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)


result_label = tk.Label(root, text="Долар США: ", font=("Arial", 14))
result_label.pack(pady=20)


root.mainloop()
