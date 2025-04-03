import tkinter as tk
from tkinter import messagebox
from materials.wallpaper import calculate_wallpaper
from materials.tile import calculate_tile
from materials.laminate import calculate_laminate
import pandas as pd

   

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Отделочные материалы")
        self.root.geometry("350x300+450+100")
        photo = tk.PhotoImage(file='du.png')
        self.root.iconphoto(False, photo)
        self.root.config(bg='#f4efe6')

        self.area_label = tk.Label(root, text="Площадь (м²):",bg='#f4efe6',fg='#162a2c')
        self.area_label.pack()
        self.area_entry = tk.Entry(root)
        self.area_entry.pack()

        self.material_label = tk.Label(root, text="Выберите материал:",bg='#f4efe6',fg='#162a2c')
        self.material_label.pack()
        self.material_var = tk.StringVar(value="wallpaper")
        tk.Radiobutton(root, text="Обои",bg='#f4efe6',fg='#162a2c', variable=self.material_var, value="wallpaper").pack()
        tk.Radiobutton(root, text="Плитка",bg='#f4efe6',fg='#162a2c', variable=self.material_var, value="tile").pack()
        tk.Radiobutton(root, text="Ламинат",bg='#f4efe6',fg='#162a2c', variable=self.material_var, value="laminate").pack()

        self.price_label = tk.Label(root, text="Цена за единицу (руб.):",bg='#f4efe6',fg='#162a2c')
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.calculate_button = tk.Button(root, text="Рассчитать",bg='#c8d9e6',fg='#162a2c', command=self.calculate)
        self.calculate_button.pack()

        self.save_button = tk.Button(root, text="Сохранить результат",bg='#567c8d',fg='#162a2c', command=self.save_report)
        self.save_button.pack()

    def calculate(self):
        try:
            area = float(self.area_entry.get())
            price = float(self.price_entry.get())

            if self.material_var.get() == "wallpaper":
                rolls_needed, total_cost = calculate_wallpaper(area, price)
                result = f"Нужно рулонов: {rolls_needed:.2f}, Общая стоимость: {total_cost:.2f} руб."
            elif self.material_var.get() == "tile":
                area_needed, total_cost = calculate_tile(area, price)
                result = f"Площадь плитки: {area_needed:.2f} м², Общая стоимость: {total_cost:.2f} руб."
            else:
                area_needed, total_cost = calculate_laminate(area, price)
                result = f"Площадь ламината: {area_needed:.2f} м², Общая стоимость: {total_cost:.2f} руб."

            messagebox.showinfo("Результат", result)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные значения.")

    def save_report(self):
        area = float(self.area_entry.get())
        price = float(self.price_entry.get())
        material_type = self.material_var.get()

        if material_type == "wallpaper":
            rolls_needed, total_cost = calculate_wallpaper(area, price)
            material_name = "Обои"
        elif material_type == "tile":
            area_needed, total_cost = calculate_tile(area, price)
            material_name = "Плитка"
        else:
            area_needed, total_cost = calculate_laminate(area, price)
            material_name = "Ламинат"

        data = {
            "Материал": [material_name],
            "Площадь (м²)": [area],
            "Цена за единицу (руб.)": [price],
            "Общая стоимость (руб.)": [total_cost]
        }

        df = pd.DataFrame(data)
        df.to_excel("report.xlsx", index=False)
        messagebox.showinfo("Сохранение", "Отчет сохранен как report.xlsx")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
