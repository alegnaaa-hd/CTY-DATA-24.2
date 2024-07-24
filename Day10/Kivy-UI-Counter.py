from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.graphics import Color, Line, RoundedRectangle

class MySlider(BoxLayout):
    def __init__(self, **kwargs):
        super(MySlider, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10  # Add padding to the BoxLayout
        self.spacing = 10
        with self.canvas.before:
            Color(1, 0, 0)  # Red color for the outline
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
            self.outline = Line(width=2, rounded_rectangle=(self.x, self.y, self.width, self.height, 10, 10, 10, 10))
            self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.outline.rounded_rectangle = (self.x, self.y, self.width, self.height, 10, 10, 10, 10)

class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a TextInput widget
        self.text_input = TextInput(size_hint=(1, 0.1))
        main_layout.add_widget(self.text_input)

        # Create a horizontal BoxLayout for sliders, buttons, and display label
        content_layout = BoxLayout(orientation='horizontal', spacing=10)

        # Create a vertical BoxLayout for sliders and labels
        slider_layout = BoxLayout(orientation='vertical', spacing=20)

        # Create sliders with labels
        for index, label_text in enumerate(["Add", "Friction Value", "Bounce Effect", "Ricochet Value"]):
            slider_box = MySlider(size_hint=(1, None), height=80)
            label = Label(text=label_text, size_hint=(1, 0.2), bold=True)
            if label_text == "Add":
                self.slider1 = Slider(min=0, max=1000, value=0, size_hint=(1, None), height=40)
                self.slider1.bind(value=self.update_display_label)
                slider_box.add_widget(label)
                slider_box.add_widget(self.slider1)
            elif label_text == "Friction Value":
                self.slider2 = Slider(min=0, max=100, value=50, size_hint=(1, None), height=40)
                self.slider2.bind(value=self.update_display_label2)
                slider_box.add_widget(label)
                slider_box.add_widget(self.slider2)
            elif label_text == "Bounce Effect":
                self.slider3 = Slider(min=0, max=100, value=50, size_hint=(1, None), height=40)
                self.slider3.bind(value=self.update_display_label3)
                slider_box.add_widget(label)
                slider_box.add_widget(self.slider3)
            elif label_text == "Ricochet Value":
                self.slider4 = Slider(min=0, max=100, value=50, size_hint=(1, None), height=40)
                self.slider4.bind(value=self.update_display_label4)
                slider_box.add_widget(label)
                slider_box.add_widget(self.slider4)

            slider_layout.add_widget(slider_box)

        # Create a vertical BoxLayout for buttons
        button_layout = BoxLayout(orientation='vertical', spacing=20)
        button_add = Button(text="Add", size_hint=(1, None), height=80)
        button_sub = Button(text="Sub", size_hint=(1, None), height=80)
        button_reset = Button(text="Reset", size_hint=(1, None), height=80)

        button_add.bind(on_press=self.on_add_click)
        button_sub.bind(on_press=self.on_sub_click)
        button_reset.bind(on_press=self.on_reset_click)

        button_layout.add_widget(button_add)
        button_layout.add_widget(button_sub)
        button_layout.add_widget(button_reset)

        # Create a vertical BoxLayout for the display labels
        display_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 1))
        self.display_label = Label(text="0", font_size=32, bold=True, size_hint=(1, 0.2))
        self.display_label2 = Label(text="50", font_size=32, bold=True, size_hint=(1, 0.2))
        self.display_label3 = Label(text="50", font_size=32, bold=True, size_hint=(1, 0.2))
        self.display_label4 = Label(text="50", font_size=32, bold=True, size_hint=(1, 0.2))
        display_layout.add_widget(Label(size_hint=(1, 0.2)))  # Spacer to center the labels
        display_layout.add_widget(self.display_label)
        display_layout.add_widget(self.display_label2)
        display_layout.add_widget(self.display_label3)
        display_layout.add_widget(self.display_label4)
        display_layout.add_widget(Label(size_hint=(1, 0.2)))  # Spacer to center the labels

        # Add vertical lines between columns
        with content_layout.canvas.before:
            Color(0, 0, 0, 1)  # Black color for the lines
            self.line1 = Line(points=(content_layout.width / 3, 0, content_layout.width / 3, content_layout.height), width=1)
            self.line2 = Line(points=(2 * content_layout.width / 3, 0, 2 * content_layout.width / 3, content_layout.height), width=1)
            content_layout.bind(size=self.update_lines)

        # Add the three vertical BoxLayouts to the horizontal BoxLayout
        content_layout.add_widget(slider_layout)
        content_layout.add_widget(button_layout)
        content_layout.add_widget(display_layout)

        # Add the horizontal BoxLayout to the main layout
        main_layout.add_widget(content_layout)

        return main_layout

    def on_add_click(self, instance):
        current_value = int(self.display_label.text)
        current_value += 1
        self.display_label.text = str(current_value)

    def on_sub_click(self, instance):
        current_value = int(self.display_label.text)
        if current_value > 0:
            current_value -= 1
        self.display_label.text = str(current_value)

    def on_reset_click(self, instance):
        self.display_label.text = "0"
        self.display_label2.text = "0"
        self.display_label3.text = "0"
        self.display_label4.text = "0"
        self.slider1.value = 0
        self.slider2.value = 0
        self.slider3.value = 0
        self.slider4.value = 0

    def update_display_label(self, instance, value):
        self.display_label.text = str(int(value))

    def update_display_label2(self, instance, value):
        self.display_label2.text = str(int(value))

    def update_display_label3(self, instance, value):
        self.display_label3.text = str(int(value))

    def update_display_label4(self, instance, value):
        self.display_label4.text = str(int(value))

    def update_lines(self, *args):
        layout = self.root.children[0]
        self.line1.points = (layout.width / 3, 0, layout.width / 3, layout.height)
        self.line2.points = (2 * layout.width / 3, 0, 2 * layout.width / 3, layout.height)

if __name__ == '__main__':
    MyApp().run()
