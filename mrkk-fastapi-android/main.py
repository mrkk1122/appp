from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

SERVICE_CLASS = "com.mrkk.fastapiserver.ServiceFastapi"

class ServerApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical", padding=24, spacing=16)
        self.status = Label(text="FastAPI: STOPPED", font_size="22sp")
        start = Button(text="START SERVER", size_hint_y=None, height=64)
        stop = Button(text="STOP SERVER", size_hint_y=None, height=64)
        start.bind(on_press=self.start_service)
        stop.bind(on_press=self.stop_service)
        box.add_widget(self.status)
        box.add_widget(start)
        box.add_widget(stop)
        return box

    def start_service(self, *_):
        try:
            from jnius import autoclass
            from android import mActivity
            Service = autoclass(SERVICE_CLASS)
            Service.start(mActivity, "")
            self.status.text = "FastAPI: RUNNING\nhttp://127.0.0.1:8000"
        except Exception as e:
            self.status.text = "START ERROR\n" + str(e)

    def stop_service(self, *_):
        try:
            from jnius import autoclass
            from android import mActivity
            Service = autoclass(SERVICE_CLASS)
            Service.stop(mActivity)
            self.status.text = "FastAPI: STOPPED"
        except Exception as e:
            self.status.text = "STOP ERROR\n" + str(e)

ServerApp().run()
