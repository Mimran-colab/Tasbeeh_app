import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from datetime import datetime

class TasbeehCounterApp(App):
    def build(self):
        self.count = 0
        self.max_count = 33  # Default max count
        self.beep_enabled = True  # Beep is enabled by default
        self.beep_sound = SoundLoader.load('tone.wav')

        main_layout = BoxLayout(orientation='vertical', padding=40, spacing=30)

        # Large clock display at the top
        self.time_label = Label(text=self.get_time(), font_size=80, halign='center', bold=True)
        Clock.schedule_interval(self.update_time, 1)  # Update time every second
        main_layout.add_widget(self.time_label)

        # Counter display with large digits, centered
        self.label = Label(text=str(self.count), font_size=250, bold=True)
        main_layout.add_widget(self.label)

        # Large Count button
        btn_count = Button(text="COUNT", font_size=80, size_hint=(1, 1), on_press=self.increment_count)
        main_layout.add_widget(btn_count)

        # Smaller button row with Reset, Set Max, and Toggle Beep
        button_row = BoxLayout(size_hint=(1, 0.2), spacing=20)

        btn_reset = Button(text="Reset", font_size=30, size_hint=(0.3, 1), on_press=self.reset_count)
        button_row.add_widget(btn_reset)

        btn_config = Button(text="Set Max", font_size=30, size_hint=(0.3, 1), on_press=self.set_max_count)
        button_row.add_widget(btn_config)

        self.btn_toggle_beep = Button(text="Beep: ON", font_size=30, size_hint=(0.3, 1), on_press=self.toggle_beep)
        button_row.add_widget(self.btn_toggle_beep)

        main_layout.add_widget(button_row)

        return main_layout

    def increment_count(self, instance):
        if self.count < self.max_count:
            self.count += 1
            self.label.text = str(self.count)
            if self.count == self.max_count and self.beep_enabled and self.beep_sound:
                self.beep_sound.play()

    def reset_count(self, instance):
        self.count = 0
        self.label.text = str(self.count)

    def set_max_count(self, instance):
        from kivy.uix.textinput import TextInput
        from kivy.uix.popup import Popup

        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.input_max = TextInput(hint_text="Enter max count", text=str(self.max_count), multiline=False, font_size=30)
        btn_save = Button(text="Save", font_size=30, on_press=self.save_max_count)
        box.add_widget(self.input_max)
        box.add_widget(btn_save)

        self.popup = Popup(title="Set Max Count", content=box, size_hint=(0.8, 0.4))
        self.popup.open()

    def save_max_count(self, instance):
        try:
            self.max_count = int(self.input_max.text)
        except ValueError:
            self.max_count = 33
        self.popup.dismiss()

    def toggle_beep(self, instance):
        self.beep_enabled = not self.beep_enabled
        if self.beep_enabled:
            self.btn_toggle_beep.text = "Beep: ON"
        else:
            self.btn_toggle_beep.text = "Beep: OFF"

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def update_time(self, dt):
        self.time_label.text = self.get_time()

if __name__ == "__main__":
    TasbeehCounterApp().run()