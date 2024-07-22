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
        self.text_input = TextInput(size_hint=(1, 0.2))
        main_layout.add_widget(self.text_input)
        # Create a horizontal BoxLayout for sliders and buttons
        content_layout = BoxLayout(orientation='horizontal', spacing=10)
        # Create a vertical BoxLayout for sliders and labels
        slider_layout = BoxLayout(orientation='vertical', spacing=20)
        # Create sliders with labels
        for label_text in ["Weight of Puck", "Friction Value", "Bounce Effect", "Ricochet Value"]:
            slider_box = MySlider(size_hint=(1, None), height=100)
            label = Label(text=label_text, size_hint=(1, 0.2), bold=True)
            slider = Slider(min=0, max=100, value=50, size_hint=(1, 0.5))
            value_label = Label(text=str(slider.value), size_hint=(1, 0.2))
            slider.bind(value=self.update_value_label(value_label))
            slider_box.add_widget(label)
            slider_box.add_widget(slider)
            slider_box.add_widget(value_label)
            slider_layout.add_widget(slider_box)
        # Create a vertical BoxLayout for buttons
        button_layout = BoxLayout(orientation='vertical', spacing=10)
        button1 = Button(text="Button 1", size_hint=(1, 0.2))
        button2 = Button(text="Button 2", size_hint=(1, 0.2))
        button3 = Button(text="Button 3", size_hint=(1, 0.2))
        button1.bind(on_press=self.on_button1_click)
        button2.bind(on_press=self.on_button2_click)
        button3.bind(on_press=self.on_button3_click)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        # Add the two vertical BoxLayouts to the horizontal BoxLayout
        content_layout.add_widget(slider_layout)
        content_layout.add_widget(button_layout)
        # Add the horizontal BoxLayout to the main layout
        main_layout.add_widget(content_layout)
        return main_layout
    def on_button1_click(self, instance):
        self.label1.text = "Button 1 clicked! Text: " + self.text_input.text
    def on_button2_click(self, instance):
        self.label2.text = "Button 2 clicked! Text: " + self.text_input.text
    def on_button3_click(self, instance):
        self.label3.text = "Button 3 clicked! Text: " + self.text_input.text
    def update_value_label(self, label):
        def update(instance, value):
            label.text = str(int(value))
        return update
if __name__ == '__main__':
    MyApp().run()
 
 