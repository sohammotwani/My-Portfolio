import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')

class AssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.lbl = Label(text="Voice Assistant Running...", font_size='20sp')
        btn = Button(text="Open YouTube Now", size_hint=(1, 0.3))
        btn.bind(on_press=self.open_yt)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def open_yt(self, instance):
        if platform == 'android':
            intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.youtube.com"))
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            PythonActivity.mActivity.startActivity(intent)

if __name__ == '__main__':
    AssistantApp().run()
