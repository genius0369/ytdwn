import sys
import os # Imported for checking if the download path exists

try:
    import yt_dlp
except ImportError:
    print("Error ❌: 'yt-dlp' module not found.")
    print("Please install it: pip install yt-dlp")
    sys.exit(1)

# --- ✨ MY DOWNLOAD FOLDER PATH ✨ ---
BASE_DOWNLOAD_PATH = '/data/data/com.termux/files/home/storage/downloads'

# Check if the specified download path exists
if not os.path.exists(BASE_DOWNLOAD_PATH):
    print(f"⚠️ Warning: Download path not found: {BASE_DOWNLOAD_PATH}")
    print(f"Please make sure the folder '{BASE_DOWNLOAD_PATH}' exists.")
    print("The script will continue, but downloads might fail.")


def get_song_quality():
    """Displays the audio quality menu and returns the user's choice."""
    print("\nSelect Quality 🎵")
    print("1. 128 kbit/s - Low 📉")
    print("2. 192 kbit/s - Medium 👍")
    print("3. 256 kbit/s - High ✨")
    print("4. 320 kbit/s - Highest 🔥")

    choice = input("Enter Your Choice : ").strip()
    quality_map = {'1': '128', '2': '192', '3': '256', '4': '320'}
    return quality_map.get(choice, '128')

def get_video_quality():
    """Displays the video quality menu and returns the format string."""
    print("\nSelect Your Video Quality. 📺")
    print("1. 240p")
    print("2. 360p")
    print("3. 480p (Default)")
    print("4. 720p")
    print("5. 1080p HD ✨")
    print("6. 1440p HD 🌟")
    print("7. 2160p HD 🚀")

    choice = input("Enter Your Choice : ").strip()
    quality_map = {
        '1': '240', '2': '360', '3': '480', '4': '720',
        '5': '1080', '6': '1440', '7': '2160'
    }
    selected_height = quality_map.get(choice, '480')
    format_string = f'bestvideo[height<=?{selected_height}]+bestaudio/best[height<=?{selected_height}]'
    return format_string, selected_height

def handle_download(ydl_opts, url, type_desc):
    """Common download handler with error checking and credit."""
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # --- ✨ UPDATED SUCCESS MESSAGE ✨ ---
        print(f"\n<-------{type_desc} Successfully Downloaded! ✅------>")
        print("<-------≈☆ Made with 💖 by Genius💞 ☆≈------->")

    except Exception as e:
        error_msg = str(e)
        if "ffmpeg is not installed" in error_msg:
            print("\n❌ CRITICAL ERROR: FFmpeg not found!")
            print("FFmpeg is required for merging high-quality (1080p+) video and audio.")
        else:
            print(f"\n❌ Download failed: {error_msg}")

def download_song():
    """Handles downloading a single song."""
    url = input("Enter Song/Video URL 🎶: ").strip()
    if not url: return

    preferred_quality = get_song_quality()
    output_template = os.path.join(BASE_DOWNLOAD_PATH, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'noplaylist': True,
        'no_warnings': True, # Keeps logs clean
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': preferred_quality,
        }],
    }
    print(f"\nDownloading audio in {preferred_quality}kbit/s... 🎧")
    handle_download(ydl_opts, url, "Song")

def download_video():
    """Handles downloading a single video."""
    url = input("Enter Video URL 🎬: ").strip()
    if not url: return

    format_string, selected_height = get_video_quality()
    output_template = os.path.join(BASE_DOWNLOAD_PATH, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': format_string,
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'no_warnings': True, # Keeps logs clean
    }
    print(f"\nDownloading video in {selected_height}p... 🍿")
    handle_download(ydl_opts, url, "Video")

def download_playlist():
    """Handles downloading a full playlist or selected items from it."""
    url = input("Enter Playlist URL 📚: ").strip()
    if not url: return

    print("\n1. Download Selected Videos. ☝️")
    print("2. Download All Videos. 🌍")
    choice = input("Enter Your Choice : ").strip()

    playlist_items = None

    if choice == '1':
        print("\nFetching playlist info (Please wait)... ⏳")
        try:
            with yt_dlp.YoutubeDL({'extract_flat': True, 'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)

            if 'entries' not in info:
                print("Playlist empty or invalid. 🤷")
                return

            print("\n--- Playlist Videos ---")
            for i, video in enumerate(info['entries']):
                print(f"{i+1}. {video.get('title', 'Unknown Title')}")
            print("-------------------------")

            selected_indices = input("Enter video numbers (comma-separated, e.g., 1,3,5) ✍️: ").strip()
            if not selected_indices:
                print("No videos selected. Aborting.")
                return
            playlist_items = selected_indices
        except Exception as e:
            print(f"Error fetching info: {e} 😥")
            return

    elif choice != '2':
        print("Invalid choice. 🚫")
        return

    format_string, selected_height = get_video_quality()
    output_template = os.path.join(BASE_DOWNLOAD_PATH, '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s')

    ydl_opts = {
        'format': format_string,
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        'no_warnings': True, # Keeps logs clean
    }

    if playlist_items:
        ydl_opts['playlist_items'] = playlist_items

    print(f"\nDownloading playlist videos in {selected_height}p... ⚡")
    handle_download(ydl_opts, url, "Playlist")

def download_multiple_videos_from_file():
    """Download multiple videos from url.txt with selected quality."""
    file_path = os.path.join(BASE_DOWNLOAD_PATH, 'url.txt')

    if not os.path.exists(file_path):
        print("❌ url.txt file Not Found")
        return

    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("❌ url.txt is empty")
        return

    format_string, selected_height = get_video_quality()
    output_template = os.path.join(BASE_DOWNLOAD_PATH, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': format_string,
        'outtmpl': output_template,
        'merge_output_format': 'mp4',
        'no_warnings': True,
        'noplaylist': True,
    }

    print(f"\nDownloading {len(urls)} videos in {selected_height}p... 🚀")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

        print("\n<-------All Videos Successfully Downloaded! ✅------>")
        print("<-------≈☆ Made with 💖 by Genius💞 ☆≈------->")

    except Exception as e:
        print(f"\n❌ Download failed: {e}")

def main():
    """Main function to run the menu loop."""
    while True:
        print("\nPlease Choose Your Choice 😊.")
        print("1. Download Song . 🎵")
        print("2. Download Video . 🎬")
        print("3. Download Playlist . 📚")
        print("4. Download multiple Videos using url.txt . 📄")
        print("Enter 'q' to quit. 🚪")

        choice = input("Enter Your choice : ").strip()

        if choice == '1': download_song()
        elif choice == '2': download_video()
        elif choice == '3': download_playlist()
        elif choice == '4': download_multiple_videos_from_file()
        elif choice.lower() == 'q':
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again. 🤔")
        print("\n" + "="*40) # Separator for clarity

if __name__ == "__main__":
    main()
