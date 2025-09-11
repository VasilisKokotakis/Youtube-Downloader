import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL
import threading
import os


def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    # Ensure Downloads folder exists
    download_folder = os.path.join(os.getcwd(), "Downloads")
    os.makedirs(download_folder, exist_ok=True)

    # Run in a separate thread so GUI doesn't freeze
    def run_download():
        try:
            ydl_opts = {
                "format": "best",
                "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),
            }
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get("title")
                views = info.get("view_count")

            messagebox.showinfo("Success", f"Downloaded:\n{title}\nViews: {views}\n\nSaved to:\n{download_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    threading.Thread(target=run_download).start()


# --- GUI setup ---
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")
root.resizable(False, False)

# Label
label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12))
label.pack(pady=10)

# Entry field
url_entry = tk.Entry(root, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download", command=download_video, font=("Arial", 12), bg="#4CAF50", fg="white")
download_button.pack(pady=20)

# Run GUI
root.mainloop()
