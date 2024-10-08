class Button:
    def __init__(self, text, button_type="Кнопка", locator=""):
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"


# Создание объектов для кнопок второго уровня вложенности
buttons = [
    Button("Text Box"),
    Button("Check Box"),
    Button("Radio Button"),
    Button("Web Tables"),
    Button("Buttons"),
    Button("Links"),
    Button("Broken Links - Images"),
    Button("Upload and Download"),
    Button("Dynamic Properties"),
]

# Вывод текста для каждой кнопки и вызов метода "клик"
for button in buttons:
    print(button.text)
    print(button.click())