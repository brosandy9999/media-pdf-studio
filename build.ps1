python -m pip install pyinstaller
python -m PyInstaller --noconfirm --onefile --windowed --add-data "webapp;webapp" --name "MediaPdfStudio" main.py
