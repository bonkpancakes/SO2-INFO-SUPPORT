[app]

# Название вашего приложения (отображается под иконкой)
title = Gemini Visuals

# Пакетное имя (только латинские буквы и цифры)
package.name = geminivisuals

# Домен компании или проекта
package.domain = org.gemini

# Директория с исходным кодом (точка означает текущую папку)
source.dir = .

# Расширения файлов, которые войдут в сборку
source.include_exts = py,png,jpg,kv,atlas

# Версия приложения
version = 0.1

# Требуемые зависимости Python
# pyjnius необходим для вызова Java API Android (включая проверку разрешений)
requirements = python3,kivy,pyjnius

# Ориентация экрана (landscape — альбомная, portrait — книжная)
orientation = landscape

# Полноэкранный режим
fullscreen = 1

# Разрешения Android
# SYSTEM_ALERT_WINDOW — разрешение на отображение поверх других окон
android.permissions = SYSTEM_ALERT_WINDOW

# Минимальная и целевая версии Android API
# API 23 соответствует Android 6.0 (требуется для управления оверлеями)
android.minapi = 23
android.api = 33

# Включает архитектуры ARM (современные смартфоны)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# Уровень логирования (2 — подробный вывод для отладки)
log_level = 2

# Предупреждать при запуске от имени root
warn_on_root = 1
