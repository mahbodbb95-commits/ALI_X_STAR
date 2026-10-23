from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.04, 0.05, 0.12, 1)


class CalculatorApp(App):

    def build(self):
        self.expression = ""

        main = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        title = Label(
            text="[b]ALI X STAR[/b]",
            markup=True,
            font_size=dp(28),
            color=(0.2, 0.6, 1, 1),
            size_hint=(1, 0.12)
        )
        main.add_widget(title)

        self.display = Label(
            text="0",
            font_size=dp(36),
            halign="right",
            valign="middle",
            size_hint=(1, 0.22),
            color=(1, 1, 1, 1)
        )
        self.display.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )
        main.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=dp(8),
            size_hint=(1, 0.66)
        )

        buttons = [
            "C", "⌫", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "±", "0", ".", "="
        ]

        for value in buttons:
            button = Button(
                text=value,
                font_size=dp(24),
                background_normal="",
                background_down="",
                background_color=self.get_color(value),
                color=(1, 1, 1, 1)
            )

            button.bind(
                on_press=lambda instance, v=value:
                self.press(v)
            )

            grid.add_widget(button)

        main.add_widget(grid)

        footer = Label(
            text="Created by ALI X STAR",
            font_size=dp(12),
            size_hint=(1, 0.06),
            color=(0.5, 0.6, 0.8, 1)
        )
        main.add_widget(footer)

        return main

    def get_color(self, value):
        if value in ("÷", "×", "-", "+", "="):
            return (0.1, 0.4, 0.9, 1)

        if value in ("C", "⌫", "%", "±"):
            return (0.25, 0.28, 0.4, 1)

        return (0.1, 0.12, 0.2, 1)

    def press(self, value):
        if value == "C":
            self.expression = ""

        elif value == "⌫":
            self.expression = self.expression[:-1]

        elif value == "±":
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = "-" + self.expression

        elif value == "%":
            try:
                number = float(self.expression)
                self.expression = str(number / 100)
            except (ValueError, TypeError):
                self.expression = ""

        elif value == "=":
            try:
                result = eval(
                    self.expression.replace("÷", "/")
                    .replace("×", "*"),
                    {"__builtins__": {}},
                    {}
                )

                if isinstance(result, (int, float)):
                    self.expression = str(result)
                else:
                    self.expression = ""

            except Exception:
                self.expression = "Error"

        else:
            if self.expression == "Error":
                self.expression = ""

            self.expression += value

        self.display.text = self.expression or "0"


if __name__ == "__main__":
    CalculatorApp().run()