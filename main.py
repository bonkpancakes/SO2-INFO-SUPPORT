from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Пытаемся импортировать модули Android через pyjnius
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Settings = autoclass('android.provider.Settings')
    Uri = autoclass('android.net.Uri')
    VERSION = autoclass('android.os.Build$VERSION')
    IS_ANDROID = True
except Exception:
    IS_ANDROID = False

class GeminiVisualsApp(App):
    def build(self):
        self.title = "Gemini Visuals Overlay"
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(
            text="[b]GEMINI VISUALS[/b]\nСтатус оверлея: Ожидание разрешения", 
            markup=True, 
            font_size='18sp',
            halign='center'
        )
        
        btn_perm = Button(
            text="1. Дать разрешение поверх окон",
            size_hint=(1, 0.25),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_perm.bind(on_press=self.request_overlay_permission)
        
        btn_effect = Button(
            text="2. Запустить эффект/прицел",
            size_hint=(1, 0.25),
            background_color=(0.9, 0.3, 0.2, 1)
        )
        btn_effect.bind(on_press=self.start_overlay_effect)
        
        layout.add_widget(self.label)
        layout.add_widget(btn_perm)
        layout.add_widget(btn_effect)
        
        return layout

    def request_overlay_permission(self, instance):
        if IS_ANDROID:
            activity = PythonActivity.mActivity
            context = activity.getApplicationContext()
            # Проверяем версию Android 6.0+ и наличие прав
            if VERSION.SDK_INT >= 23:
                if not Settings.canDrawOverlays(context):
                    intent = Intent(
                        Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                        Uri.parse("package:" + context.getPackageName())
                    )
                    activity.startActivity(intent)
                    self.label.text = "Разреши поверх других окон\nв настройках и вернись!"
                else:
                    self.label.text = "Доступ уже предоставлен!"
        else:
            self.label.text = "Это работает только на Android устройстве!"

    def start_overlay_effect(self, instance):
        if IS_ANDROID:
            context = PythonActivity.mActivity.getApplicationContext()
            if VERSION.SDK_INT >= 23 and Settings.canDrawOverlays(context):
                self.label.text = "Оверлей активен! (Здесь будет отрисовка)"
                # В будущем здесь запускается фоновый сервис с WindowManager для рисования прицела/эффекта
            else:
                self.label.text = "Сначала дай разрешение кнопкой выше!"
        else:
            self.label.text = "Тестовый режим на ПК"

if __name__ == '__main__':
    GeminiVisualsApp().run()
