
# 🎬 Modern YouTube Downloader GUI

A lightweight yet polished Python app to download YouTube videos using **yt-dlp**, featuring a modern **ttkbootstrap** interface, video previews, and real-time progress updates.


## ✨ Features

- 🎥 **Preview before download** — shows the video’s title and thumbnail.
- ⚡ **Modern themed UI** with `ttkbootstrap` (dark or light modes).
- 📊 **Live progress bar** with percentage updates.
- 🧵 **Threaded downloads** to keep the GUI fully responsive.
- 💾 **Auto-saves videos** in a local `Downloads/` folder inside the project.
- 🔍 **Displays title and view count** after download completes.


## 🚀 Installation & Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/VasilisKokotakis/Youtube-Downloader.git
   cd Youtube-Downloader

2. **Install dependencies**
   Make sure you have Python 3.8+ installed, then run:

   ```bash
   pip install yt-dlp ttkbootstrap pillow requests
   ```

   `tkinter` usually comes pre-installed.
   If not (on Debian/Ubuntu):

   ```bash
   sudo apt install python3-tk
   ```

3. **Run the app**

   ```bash
   python main.py
   ```

   The app window will open with a clean modern UI, ready to paste a YouTube URL, preview, and download.

## 📸 Screenshot

<img width="477" height="527" alt="image" src="https://github.com/user-attachments/assets/0f64e301-edd7-45ff-80c2-6a10bee890b6" />
<img width="477" height="527" alt="image" src="https://github.com/user-attachments/assets/29a4befb-0421-4242-ad88-b3015ea990fc" />
<img width="477" height="527" alt="image" src="https://github.com/user-attachments/assets/60b193ab-104b-48b8-aa9b-a40561ba8268" />



## 📂 Project Structure

```
.
├── Downloads/        # Downloaded videos (auto-created)
├── assets/           # Optional folder for screenshots
├── main.py           # Main application code
└── README.md         # Project documentation
```

## ⚠️ Disclaimer

This tool is for **personal use only**.
Please respect YouTube’s Terms of Service and download only videos you have the rights to.

## 📜 License

MIT License — free to use, modify, and share.
