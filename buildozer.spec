[app]

# (str) Title of your application
title = Voice Assistant

# (str) Package name
package.name = voiceassistant

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
`buildozer.spec` file ka poora aur sahi configuration code niche diya gaya hai. Isme aapke app ke saare permissions aur settings (jaise SDK license accept karna aur API version) pehle se configured hain.

Apni repository me `buildozer.spec` file ko edit karke ye poora code paste kar do:

```ini
[app]

# App ka naam
title = Voice Assistant

# App ka package name (bina space ke)
package.name = voiceassistant

# Package domain
package.domain = org.test

# Source code location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 0.1

# Application requirements (Kivy aur Python modules)
requirements = python3,kivy,pyjnius

# Supported orientations
orientation = portrait

# Fullscreen setting (0 = No, 1 = Yes)
fullscreen = 0

# Android Permissions (Voice & Internet ke liye)
android.permissions = INTERNET, RECORD_AUDIO, FOREGROUND_SERVICE

# Android API Settings
android.api = 33
android.minapi = 21
android.sdk_build_tools_version = 33.0.2

# Automatically Accept Android SDK Licenses
android.accept_sdk_license = True

# NDK version
android.ndk = 25b

# Architecture
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# Log level (2 = debug)
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1
