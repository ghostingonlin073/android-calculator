[app]
title = Калькулятор
package.name = calculator
package.domain = org.calculator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0.0
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[app]
presplash.filename = %(source.dir)s/assets/presplash.png
icon.filename = %(source.dir)s/assets/icon.png

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.gradle_dependencies = 'com.android.tools.build:gradle:7.2.2'

android.allow_backup = True
android.filename = Calculator-v1.0.0.apk

[app:source.exclude_patterns]
.git,.github,.gitignore,README.md,*.spec,venv

p4a.branch = master
