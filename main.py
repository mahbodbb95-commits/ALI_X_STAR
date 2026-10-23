from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#101827")


class CalculatorApp(App):

    def build(self):
        self.expression = ""

        main = BoxLayout(
            orientation="vertical",
            padding=12,
            spacing=10
        )

        title = Label(
            text="ALI X STAR",
            font_size=26,
            size_hint_y=0.15,
            color=(0.2, 0.7, 1, 1)
        )
        main.add_widget(title)

        self.display = Label(
            text="0",
            font_size=38,
            size_hint_y=0.25,
            halign="right",
            valign="middle"
        )
        main.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=7
        )

        buttons = [
            "C", "⌫", "/", "*",
            "7", "8", "9", "-",
            "4", "5", "6", "+",
            "1", "2", "3", "=",
            "0", ".", "00", "="
        ]

        for value in buttons:
            button = Button(
                text=value,
                font_size=24,
                background_normal="",
                background_color=(
                    (0.12, 0.42, 0.75, 1)
                    if value in ["+", "-", "*", "/", "="]
                    else (0.15, 0.20, 0.30, 1)
                )
            )

            button.bind(on_press=self.press)
            grid.add_widget(button)

        main.add_widget(grid)
        return main

    def press(self, button):
        value = button.text

        if value == "C":
            self.expression = ""
            self.display.text = "0"

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.display.text = self.expression or "0"

        elif value == "=":
            try:
                allowed = "0123456789+-*/. "
                if not self.expression or any(
                    c not in allowed for c in self.expression
                ):
                    self.display.text = "Error"
                    return

                result = eval(self.expression, {"__builtins__": {}}, {})
                self.expression = str(result)
                self.display.text = self.expression

            except Exception:
                self.display.text = "Error"
                self.expression = ""

        else:
            self.expression += value
            self.display.text = self.expression


CalculatorApp().run()
