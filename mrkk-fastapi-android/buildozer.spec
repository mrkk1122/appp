[app]
title = MRKK FastAPI Server
package.name = fastapiserver
package.domain = com.mrkk
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,txt
version = 1.0.0
requirements = python3,kivy,fastapi,uvicorn,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,FOREGROUND_SERVICE,FOREGROUND_SERVICE_DATA_SYNC,POST_NOTIFICATIONS,WAKE_LOCK
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
services = Fastapi:services/fastapi_service.py:foreground:sticky

[buildozer]
log_level = 2
warn_on_root = 1
