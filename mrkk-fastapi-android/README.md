# MRKK FastAPI Android Server

Android app starter that embeds Python/FastAPI and runs Uvicorn through an Android foreground/sticky service.

## Build without Android Studio
1. Create a new GitHub repository, e.g. `mrkk-fastapi-android`.
2. Upload this entire project to the repository.
3. Push to the `main` branch.
4. Open **Actions** → **Build MRKK FastAPI APK** → **Run workflow**.
5. Wait for the build to finish.
6. Open the successful workflow run and download the artifact **mrkk-fastapi-server-apk**.
7. Extract the ZIP and install the APK on your Android phone.

## Run
Open the app and tap **START SERVER**. The API listens on port 8000.

Phone: `http://127.0.0.1:8000`

Same Wi-Fi from another device: `http://PHONE_IP:8000`

Health check: `/health`

## Replace the API
Edit `app/main.py` with your own FastAPI routes and push again. GitHub Actions will build a new APK.

## Screen-off note
The app uses a foreground/sticky service, but Android and OEM battery management can still stop background processes. After installing, allow notifications and set the app's battery usage to **Unrestricted** (wording varies by Android/MIUI/HyperOS).

This is not a guarantee of 24/7 uptime.
