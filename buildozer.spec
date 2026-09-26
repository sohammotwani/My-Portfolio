[app]

# App details
title = Voice Assistant
package.name = voiceassistant
package.domain = org.test

# Source code
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 0.1

# Requirements
requirements = python3,kivy,pyjnius

# Screen settings
orientation = portrait
fullscreen = 0

# Android Permissions
android.permissions = INTERNET, RECORD_AUDIO, FOREGROUND_SERVICE

# Android API & Build Tools
android.api = 33
android.minapi = 21
android.sdk_build_tools_version = 33.0.2

# Accept Licenses Automatically
android.accept_sdk_license = True

# NDK & Architecture
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
