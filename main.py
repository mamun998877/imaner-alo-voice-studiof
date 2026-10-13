from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

Window.clearcolor = (0.025, 0.07, 0.13, 1)


class VoiceStudio(App):

    def build(self):
        self.title = "Imaner Alo Voice Studio"

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=14
        )

        root.add_widget(Label(
            text="[b]Imaner Alo BD[/b]",
            markup=True,
            font_size="28sp",
            color=(1, 0.78, 0.35, 1),
            size_hint_y=None,
            height=65
        ))

        root.add_widget(Label(
            text="ADVANCED AI STUDIO",
            font_size="14sp",
            color=(0.8, 0.88, 1, 1),
            size_hint_y=None,
            height=30
        ))

        root.add_widget(Label(
            text="আপনার ভিডিওর স্ক্রিপ্ট লিখুন",
            font_size="17sp",
            size_hint_y=None,
            height=40
        ))

        self.script = TextInput(
            hint_text="এখানে বাংলা স্ক্রিপ্ট লিখুন...",
            multiline=True,
            font_size="17sp",
            background_color=(0.07, 0.14, 0.23, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 0.78, 0.35, 1),
            padding=12
        )

        root.add_widget(self.script)

        self.voice = Spinner(
            text="বাংলা পুরুষ কণ্ঠ",
            values=(
                "বাংলা পুরুষ কণ্ঠ",
                "বাংলা নারী কণ্ঠ"
            ),
            size_hint_y=None,
            height=50
        )

        root.add_widget(self.voice)

        self.status = Label(
            text="আপনার AI Studio প্রস্তুত",
            font_size="14sp",
            size_hint_y=None,
            height=45
        )

        voice_btn = Button(
            text="🎙️ Generate Voice",
            size_hint_y=None,
            height=55,
            background_normal="",
            background_color=(0.84, 0.64, 0.25, 1),
            color=(0.03, 0.07, 0.12, 1)
        )
        voice_btn.bind(on_press=self.generate_voice)
        root.add_widget(voice_btn)

        image_btn = Button(
            text="🖼️ AI Image Generator",
            size_hint_y=None,
            height=50
        )
        image_btn.bind(on_press=self.generate_image)
        root.add_widget(image_btn)

        video_btn = Button(
            text="🎬 AI Video Studio",
            size_hint_y=None,
            height=50
        )
        video_btn.bind(on_press=self.generate_video)
        root.add_widget(video_btn)

        root.add_widget(self.status)

        return root

    def generate_voice(self, instance):
        text = self.script.text.strip()

        if not text:
            self.status.text = "প্রথমে স্ক্রিপ্ট লিখুন।"
            return

        self.status.text = (
            "স্ক্রিপ্ট প্রস্তুত। "
            "AI Voice API সংযুক্ত করা প্রয়োজন।"
        )

    def generate_image(self, instance):
        self.status.text = (
            "AI Image API এখনো সংযুক্ত করা হয়নি।"
        )

    def generate_video(self, instance):
        self.status.text = (
            "Video Engine পরবর্তী ধাপে যুক্ত হবে।"
        )


if __name__ == "__main__":
    VoiceStudio().run()
