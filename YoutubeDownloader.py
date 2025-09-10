from yt_dlp import YoutubeDL

def main():
    # Ask user for URL
    url = input("Enter the YouTube URL: ")

    # yt-dlp options
    ydl_opts = {
        "format": "best",                  # best quality
        "outtmpl": "%(title)s.%(ext)s",    # save file as video title
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            print("Title:", info.get("title"))
            print("Views:", info.get("view_count"))
            print("Download complete.")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
