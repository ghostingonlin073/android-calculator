from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class CalculatorApp(App):
    def build(self):
        # Устанавливаем размер окна для мобильных устройств
        Window.size = (350, 550)
        self.title = "Простой калькулятор"
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # Заголовок
        title_label = Label(
            text="Калькулятор",
            font_size='24sp',
            size_hint=(1, 0.1),
            color=get_color_from_hex('#2E7D32')
        )
        main_layout.add_widget(title_label)
        
        # Поле ввода/вывода
        self.display = TextInput(
            multiline=False, 
            readonly=False,
            halign='right',
            font_size='32sp',
            size_hint=(1, 0.15),
            background_color=get_color_from_hex('#E8F5E8'),
            foreground_color=get_color_from_hex('#1B5E20')
        )
        main_layout.add_widget(self.display)
        
        # Создаем кнопки калькулятора
        buttons_grid = BoxLayout(orientation='vertical', spacing=8)
        
        # Первый ряд
        buttons_row1 = BoxLayout(spacing=8)
        buttons_row1.add_widget(self.create_button('7'))
        buttons_row1.add_widget(self.create_button('8'))
        buttons_row1.add_widget(self.create_button('9'))
        buttons_row1.add_widget(self.create_operator_button('/'))
        buttons_grid.add_widget(buttons_row1)
        
        # Второй ряд
        buttons_row2 = BoxLayout(spacing=8)
        buttons_row2.add_widget(self.create_button('4'))
        buttons_row2.add_widget(self.create_button('5'))
        buttons_row2.add_widget(self.create_button('6'))
        buttons_row2.add_widget(self.create_operator_button('*'))
        buttons_grid.add_widget(buttons_row2)
        
        # Третий ряд
        buttons_row3 = BoxLayout(spacing=8)
        buttons_row3.add_widget(self.create_button('1'))
        buttons_row3.add_widget(self.create_button('2'))
        buttons_row3.add_widget(self.create_button('3'))
        buttons_row3.add_widget(self.create_operator_button('-'))
        buttons_grid.add_widget(buttons_row3)
        
        # Четвертый ряд
        buttons_row4 = BoxLayout(spacing=8)
        buttons_row4.add_widget(self.create_button('0'))
        buttons_row4.add_widget(self.create_button('.'))
        buttons_row4.add_widget(self.create_calculate_button('='))
        buttons_row4.add_widget(self.create_operator_button('+'))
        buttons_grid.add_widget(buttons_row4)
        
        # Пятый ряд (управление)
        buttons_row5 = BoxLayout(spacing=8)
        buttons_row5.add_widget(self.create_clear_button('C'))
        buttons_row5.add_widget(self.create_delete_button('⌫'))
        buttons_grid.add_widget(buttons_row5)
        
        main_layout.add_widget(buttons_grid)
        
        return main_layout
    
    def create_button(self, text):
        button = Button(
            text=text,
            font_size='20sp',
            background_color=get_color_from_hex('#4CAF50'),
            background_normal=''
        )
        button.bind(on_press=self.on_button_press)
        return button
    
    def create_operator_button(self, text):
        button = Button(
            text=text,
            font_size='20sp',
            background_color=get_color_from_hex('#FF9800'),
            background_normal=''
        )
        button.bind(on_press=self.on_button_press)
        return button
    
    def create_calculate_button(self, text):
        button = Button(
            text=text,
            font_size='20sp',
            background_color=get_color_from_hex('#2196F3'),
            background_normal=''
        )
        button.bind(on_press=self.on_button_press)
        return button
    
    def create_clear_button(self, text):
        button = Button(
            text=text,
            font_size='20sp',
            background_color=get_color_from_hex('#F44336'),
            background_normal='',
            size_hint=(0.5, 1)
        )
        button.bind(on_press=self.on_button_press)
        return button
    
    def create_delete_button(self, text):
        button = Button(
            text=text,
            font_size='20sp',
            background_color=get_color_from_hex('#FF5722'),
            background_normal='',
            size_hint=(0.5, 1)
        )
        button.bind(on_press=self.on_button_press)
        return button
    
    def on_button_press(self, instance):
        current_text = self.display.text
        button_text = instance.text
        
        if button_text == '=':
            try:
                # Заменяем символы для корректного вычисления
                expression = current_text.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.display.text = result
            except ZeroDivisionError:
                self.display.text = 'Ошибка: деление на 0'
            except Exception as e:
                self.display.text = 'Ошибка вычисления'
        elif button_text == 'C':
            self.display.text = ''
        elif button_text == '⌫':
            self.display.text = current_text[:-1]
        else:
            # Заменяем символы для отображения
            display_text = button_text
            if button_text == '*':
                display_text = '×'
            elif button_text == '/':
                display_text = '÷'
            
            self.display.text = current_text + display_text

if __name__ == '__main__':
    CalculatorApp().run()
