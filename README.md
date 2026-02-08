📘 README.md (Complete & Professional)
Copy code
Markdown

🎬🎵 Universal yt-dlp Downloader (Windows • Linux • Termux)

An interactive Python-based downloader script powered by yt-dlp, supporting:

🎵 MP3 audio downloads (128–320 kbps)

🎬 Video downloads (240p → 2160p / 4K)

📚 Full playlists or selected playlist items

📄 Batch downloads using url.txt

🧠 Clean menu-driven interface


Works on:

🪟 Windows

🐧 Linux

🤖 Android (Termux)



---

✨ Features

Simple terminal UI

Audio & video quality selector

Playlist index selection

Auto video+audio merge (MP4)

FFmpeg-powered audio extraction

Safe & stable yt-dlp backend



---

📦 Requirements

🔹 Common (All Platforms)

Python 3.8+

yt-dlp

FFmpeg (mandatory for merging & MP3)



---

🪟 Windows Installation

1️⃣ Install Python

Download & install from:
https://www.python.org/downloads/
Copy code

✔️ Enable “Add Python to PATH”

Check:

python --version  
2️⃣ Install yt-dlp  
Copy code  
Powershell  
pip install -r requirements.txt  
3️⃣ Install FFmpeg (IMPORTANT ⚠️)  
Method 1: Chocolatey (Recommended)  
Copy code  
Powershell  
choco install ffmpeg  
Method 2: Manual  
Download from: https://ffmpeg.org/download.html  
Extract  
Add bin folder to PATH  
Verify:  
Copy code  
Powershell  
ffmpeg -version  
🐧 Linux Installation (Ubuntu / Debian)  
1️⃣ Install Python & pip  
Copy code  
Bash  
sudo apt update  
sudo apt install python3 python3-pip -y  
2️⃣ Install yt-dlp  
Copy code  
Bash  
pip3 install -r requirements.txt  
3️⃣ Install FFmpeg  
Copy code  
Bash  
sudo apt install ffmpeg -y  
Verify:  
Copy code  
Bash  
ffmpeg -version  
🤖 Termux (Android) Installation  
1️⃣ Update & Install Python  
Copy code  
Bash  
pkg update && pkg upgrade -y  
pkg install python -y  
2️⃣ Storage Permission  
Copy code  
Bash  
termux-setup-storage  
3️⃣ Install yt-dlp  
Copy code  
Bash  
pip install -r requirements.txt  
4️⃣ Install FFmpeg  
Copy code  
Bash  
pkg install ffmpeg -y  
Verify:  
Copy code  
Bash  
ffmpeg -version  
📁 Download Location  
Termux  
Copy code  
  
/data/data/com.termux/files/home/storage/downloads  
Windows / Linux  
Copy code  
  
Current script directory  
🚀 How to Run Script  
Windows  
Copy code  
Powershell  
python downloader.py  
Linux  
Copy code  
Bash  
python3 downloader.py  
Termux  
Copy code  
Bash  
python downloader.py  
📜 Menu Options  
Copy code  
  
1. Download Song 🎵  
2. Download Video 🎬  
3. Download Playlist 📚  
4. Download multiple videos using url.txt 📄  
q. Quit 🚪  
🎵 Audio Download (MP3)  
Input: YouTube / supported site URL  
Choose bitrate:  
128 kbps  
192 kbps  
256 kbps  
320 kbps  
Output: .mp3  
🎬 Video Download  
Select resolution (240p → 2160p)  
Best audio + best video auto-merged  
Output: .mp4  
📚 Playlist Download  
Choose:  
🌍 Full playlist  
☝️ Selected items (e.g. 1,4,7)  
Output structure:  
Copy code  
  
Playlist Name/  
 ├── 01 - Title.mp4  
 ├── 02 - Title.mp4  
📄 Batch Download using url.txt  
1️⃣ Create file  
Copy code  
  
url.txt  
2️⃣ Add URLs (one per line)  
Copy code  
  
https://youtube.com/...  
https://youtube.com/...  
3️⃣ Choose option 4 from menu  
❌ Common Errors & Fixes  
❌ FFmpeg not found  
Solution:  
Install FFmpeg  
Restart terminal  
❌ Permission denied (Termux)  
Copy code  
Bash  
termux-setup-storage  

❤️ Credits    
Made with 💖 by Genius 💞 
Backend powered by yt-dlp  
  
