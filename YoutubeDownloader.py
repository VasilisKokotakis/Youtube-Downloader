import os
import threading
import requests
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Frame, Label, Entry, Button, Progressbar
from yt_dlp import YoutubeDL


# --- Core Functions ---
def fetch_video_info(url):
    try:
        with YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
        return info
    except Exception:
        return None


def show_preview(info):
    if not info:
        messagebox.showerror("Error", "Could not fetch video info.")
        return

    title = info.get("title", "Unknown Title")
    thumbnail_url = info.get("thumbnail")

    # Set title text
    title_label.config(text=title[:60] + "..." if len(title) > 60 else title)

    # Fetch and show thumbnail
    if thumbnail_url:
        try:
            response = requests.get(thumbnail_url, timeout=5)
            img_data = Image.open(BytesIO(response.content))
            img_data = img_data.resize((200, 120))
            tk_img = ImageTk.PhotoImage(img_data)
            thumbnail_label.config(image=tk_img)
            thumbnail_label.image = tk_img
        except Exception:
            thumbnail_label.config(image="", text="No thumbnail")


def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    # Reset progress
    progress_var.set(0)
    progress_label.config(text="Starting download...")

    # Ensure project-specific Downloads folder exists
    download_folder = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(download_folder, exist_ok=True)

    def run_download():
        try:
            def progress_hook(d):
                if d["status"] == "downloading":
                    total = d.get("total_bytes") or d.get("total_bytes_estimate")
                    downloaded = d.get("downloaded_bytes", 0)
                    if total:
                        percent = downloaded / total * 100
                        progress_var.set(percent)
                        progress_label.config(text=f"Downloading... {percent:.1f}%")
                elif d["status"] == "finished":
                    progress_var.set(100)
                    progress_label.config(text="Processing...")

            ydl_opts = {
                "format": "best",
                "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),
                "progress_hooks": [progress_hook],
                "quiet": True,
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get("title")
                views = info.get("view_count")

            root.after(0, lambda: messagebox.showinfo(
                "Success",
                f"Downloaded:\n{title}\nViews: {views:,}\n\nSaved to:\n{download_folder}"
            ))
            root.after(0, lambda: progress_label.config(text="Download complete!"))
        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Error", f"An error occurred:\n{str(e)}"))
            root.after(0, lambda: progress_label.config(text="Download failed."))

    threading.Thread(target=run_download, daemon=True).start()


def preview_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    progress_label.config(text="Fetching video info...")
    threading.Thread(
        target=lambda: show_preview(fetch_video_info(url)),
        daemon=True
    ).start()


# --- GUI setup ---
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("480x500")
root.resizable(False, False)

style = Style(theme="flatly")  # You can try “superhero”, “cyborg”, “darkly”, etc.

main_frame = Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

Label(main_frame, text="Enter YouTube URL:", font=("Helvetica", 12)).pack(pady=10)

url_entry = Entry(main_frame, width=50, font=("Helvetica", 10))
url_entry.pack(pady=5)

btn_frame = Frame(main_frame)
btn_frame.pack(pady=10)

Button(btn_frame, text="Preview", bootstyle="info", command=preview_video).pack(side="left", padx=5)
Button(btn_frame, text="Download", bootstyle="success", command=download_video).pack(side="left", padx=5)

# Thumbnail preview
thumbnail_label = Label(main_frame, text="No thumbnail", bootstyle="secondary", anchor="center")
thumbnail_label.pack(pady=10)

# Title
title_label = Label(main_frame, text="", font=("Helvetica", 11, "bold"), wraplength=400)
title_label.pack(pady=5)

# Progress bar + text
progress_var = tk.DoubleVar()
Progressbar(main_frame, length=400, variable=progress_var, maximum=100).pack(pady=10)
progress_label = Label(main_frame, text="Waiting...", font=("Helvetica", 10))
progress_label.pack(pady=5)

root.mainloop()
