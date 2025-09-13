```markdown
# Simple YouTube Downloader GUI

A lightweight Python app to download YouTube videos using **yt-dlp** with a user-friendly interface built on **tkinter**.

---

### ✨ Features
- Paste a YouTube URL and download with one click
- Downloads the best available video quality
- Saves files in a local `Downloads` folder inside the project directory
- Displays video title and view count after download
- GUI stays responsive thanks to threading

---

### 🚀 Installation & Usage

1. **Clone the repo**
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**

   Make sure you have Python 3.8+ installed. Then run:
   ```
   pip install yt-dlp
   ```

   `tkinter` usually comes pre-installed with Python.  
   If not, install it via your package manager (e.g. for Debian/Ubuntu):
   ```
   sudo apt install python3-tk
   ```

3. **Run the app**
   ```
   python main.py
   ```

---

### 📂 Project Structure
```
.
├── Downloads/        # Downloaded videos (auto-created)
├── main.py           # Main application code
└── README.md         # Project documentation
```

---

### ⚠️ Disclaimer

This tool is for personal use only. Please respect YouTube’s Terms of Service and only download videos you have the right to.

---

### 📜 License

MIT License — feel free to use, modify, and share.
```
