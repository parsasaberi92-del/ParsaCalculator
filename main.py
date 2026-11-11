
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):
    def build(self):
        self.expression = ""

        layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=8
        )

        self.display = Label(
            text="0",
            font_size=45,
            size_hint=(1, 0.25)
        )

        layout.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            line = BoxLayout(spacing=5)

            for char in row:
                btn = Button(
                    text=char,
                    font_size=30
                )
                btn.bind(
                    on_press=self.press
                )
                line.add_widget(btn)

            layout.add_widget(line)

        return layout

    def press(self, button):
        char = button.text

        if char == "C":
            self.expression = ""
            self.display.text = "0"

        elif char == "=":
            try:
                result = eval(
                    self.expression,
                    {"__builtins__": {}},
                    {}
                )
                self.expression = str(result)
                self.display.text = self.expression
            except Exception:
                self.expression = ""
                self.display.text = "Error"

        else:
            self.expression += char
            self.display.text = self.expression


Calculator().run()
