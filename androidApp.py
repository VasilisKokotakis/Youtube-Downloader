from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from yt_dlp import YoutubeDL
import threading
import os


class DownloaderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15

        # Input field
        self.url_input = TextInput(
            hint_text="Enter YouTube URL",
            multiline=False,
            size_hint=(1, 0.2),
        )
        self.add_widget(self.url_input)

        # Download button
        self.download_btn = Button(
            text="Download Video",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.7, 0.3, 1),  # green
        )
        self.download_btn.bind(on_press=self.download_video)
        self.add_widget(self.download_btn)

        # Status label
        self.status_label = Label(
            text="Ready.",
            size_hint=(1, 0.2),
        )
        self.add_widget(self.status_label)

    def set_status(self, message):
        # Use Clock to update UI safely from threads
        Clock.schedule_once(lambda dt: setattr(self.status_label, "text", message))

    def download_video(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.set_status("Please enter a URL.")
            return

        self.set_status("Downloading...")

        # Ensure Downloads folder exists
        download_folder = os.path.join(os.getcwd(), "Downloads")
        os.makedirs(download_folder, exist_ok=True)

        def run_download():
            try:
                ydl_opts = {
                    "format": "best",
                    "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),
                    "quiet": True,             # disable verbose logging
                    "no_warnings": True,       # suppress warnings
                }
                with YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    title = info.get("title")
                self.set_status(f"Downloaded: {title}")
            except Exception as e:
                self.set_status(f"Error: {str(e)}")

        threading.Thread(target=run_download).start()


class YouTubeDownloaderApp(App):
    def build(self):
        return DownloaderLayout()


if __name__ == "__main__":
    YouTubeDownloaderApp().run()
