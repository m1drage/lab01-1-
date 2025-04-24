
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from materials.wallpaper import Wallpaper
from materials.tile import Tile
from materials.laminate import Laminate

class MaterialApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.material_spinner = Spinner(
            text='Выберите материал',
            values=('Обои', 'Плитка', 'Ламинат')
        )
        self.add_widget(self.material_spinner)

        self.length_input = TextInput(hint_text="Длина (м)", multiline=False, input_filter='float')
        self.width_input = TextInput(hint_text="Ширина (м)", multiline=False, input_filter='float')
        self.add_widget(self.length_input)
        self.add_widget(self.width_input)

        self.calculate_button = Button(text='Рассчитать')
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.result_label = Label(text='Результат')
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            length = float(self.length_input.text)
            width = float(self.width_input.text)
            material_type = self.material_spinner.text

            if material_type == 'Обои':
                material = Wallpaper(length, width)
            elif material_type == 'Плитка':
                material = Tile(length, width)
            elif material_type == 'Ламинат':
                material = Laminate(length, width)
            else:
                self.result_label.text = 'Пожалуйста, выберите материал'
                return
            print(str(material))

            area = material.calculate_area()
            cost = material.calculate_cost()
            self.result_label.text = f"{str(material)}: {area:.2f} кв.м Стоимость: {cost:.2f} руб."
        except ValueError:
            self.result_label.text = "Введите корректные значения."

class MainApp(App):
    def build(self):
        return MaterialApp()

if __name__ == '__main__':
    MainApp().run()

