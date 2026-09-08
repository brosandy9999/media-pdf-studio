import os
import sys
import threading
import webbrowser
import http.server
import socketserver
import tkinter as tk
from tkinter import messagebox

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(get_base_path(), 'webapp'), **kwargs)
    def log_message(self, format, *args):
        pass  # Suppress console logging

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

def start_server():
    for port in range(4173, 4220):
        try:
            httpd = ThreadingTCPServer(("127.0.0.1", port), QuietHandler)
            thread = threading.Thread(target=httpd.serve_forever, daemon=True)
            thread.start()
            return port, httpd
        except OSError:
            continue
    raise RuntimeError("Could not bind to any local port in range 4173-4220.")

def main():
    try:
        port, httpd = start_server()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start local server:\n{e}")
        return

    app_url = f"http://127.0.0.1:{port}/"
    
    # Open browser automatically
    webbrowser.open(app_url)

    # Simple Control GUI
    root = tk.Tk()
    root.title("Media PDF Studio")
    root.geometry("460x230")
    root.resizable(False, False)
    root.configure(bg="#101418")

    frame = tk.Frame(root, bg="#101418", padx=22, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

    lbl_title = tk.Label(frame, text="Media PDF Studio", font=("Segoe UI", 16, "bold"), fg="#20b2aa", bg="#101418")
    lbl_title.pack(anchor="w", pady=(0, 4))

    lbl_desc = tk.Label(frame, text="Offline Interactive PDF Studio is active & running.", font=("Segoe UI", 10), fg="#eef2f6", bg="#101418")
    lbl_desc.pack(anchor="w", pady=(0, 2))

    lbl_url = tk.Label(frame, text=f"Local Address: {app_url}", font=("Segoe UI", 10, "underline"), fg="#9ba8b8", bg="#101418", cursor="hand2")
    lbl_url.pack(anchor="w", pady=(0, 16))
    lbl_url.bind("<Button-1>", lambda e: webbrowser.open(app_url))

    btn_frame = tk.Frame(frame, bg="#101418")
    btn_frame.pack(fill=tk.X, pady=6)

    btn_open = tk.Button(btn_frame, text="Open in Browser", font=("Segoe UI", 10, "bold"), bg="#19948d", fg="#ffffff", activebackground="#20b2aa", bd=0, padx=16, pady=8, cursor="hand2", command=lambda: webbrowser.open(app_url))
    btn_open.pack(side=tk.LEFT, padx=(0, 10))

    btn_exit = tk.Button(btn_frame, text="Stop & Exit", font=("Segoe UI", 10), bg="#26303a", fg="#eef2f6", bd=0, padx=16, pady=8, cursor="hand2", command=root.destroy)
    btn_exit.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
