# 🎬🎵 Universal yt-dlp Downloader  
**(Windows • Linux • Termux)**

An interactive **Python-based downloader script** powered by **yt-dlp**, supporting high-quality audio & video downloads with a clean, menu-driven interface.

---

## 🔥 Supported Downloads

- 🎵 **MP3 Audio** (128 / 192 / 256 / 320 kbps)
- 🎬 **Video** (240p → 2160p / 4K)
- 📚 **Playlists** (full or selective items)
- 📄 **Batch downloads** using `url.txt`
- 🧠 Easy & clean **interactive menu**

---

## 🖥️ Works On

- 🪟 Windows  
- 🐧 Linux  
- 🤖 Android (Termux)

---

## ✨ Features

- Simple terminal UI
- Audio & video quality selector
- Playlist index selection
- Auto **video + audio merge** (MP4)
- **FFmpeg-powered** MP3 extraction
- Safe & stable **yt-dlp backend**

---

## 📦 Requirements

### 🔹 Common (All Platforms)

- Python **3.8+**
- `yt-dlp`
- **FFmpeg** (mandatory for merging & MP3)

---

## 🪟 Windows Installation

### 1️⃣ Install Python  
Download from:  
https://www.python.org/downloads/

✔️ Enable **“Add Python to PATH”**

Verify:
```powershell
python --version
```

### 2️⃣ Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg ⚠️ (IMPORTANT)

#### Method 1: Chocolatey (Recommended)
```powershell
choco install ffmpeg
```

#### Method 2: Manual
- Download: https://ffmpeg.org/download.html  
- Extract  
- Add `bin` folder to **PATH**

Verify:
```powershell
ffmpeg -version
```

---

## 🐧 Linux Installation (Ubuntu / Debian)

### 1️⃣ Install Python & pip
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2️⃣ Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 3️⃣ Install FFmpeg
```bash
sudo apt install ffmpeg -y
```

Verify:
```bash
ffmpeg -version
```

---

## 🤖 Termux (Android) Installation

### 1️⃣ Update & Install Python
```bash
pkg update && pkg upgrade -y
pkg install python -y
```

### 2️⃣ Storage Permission
```bash
termux-setup-storage
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install FFmpeg
```bash
pkg install ffmpeg -y
```

Verify:
```bash
ffmpeg -version
```

---

## 📁 Download Location

### 📱 Termux
```
/data/data/com.termux/files/home/storage/downloads
```

### 🖥️ Windows / Linux
```
Current script directory
```

---

## 🚀 How to Run

### Windows
```powershell
python downloader.py
```

### Linux
```bash
python3 downloader.py
```

### Termux
```bash
python downloader.py
```

---

## 📜 Menu Options

```
1. Download Song 🎵
2. Download Video 🎬
3. Download Playlist 📚
4. Download multiple videos using url.txt 📄
q. Quit 🚪
```

---

## 🎵 Audio Download (MP3)

- Input: YouTube / supported site URL  
- Select bitrate:
  - 128 kbps
  - 192 kbps
  - 256 kbps
  - 320 kbps  
- Output: `.mp3`

---

## 🎬 Video Download

- Select resolution (240p → 2160p)
- Best audio + best video auto-merged
- Output: `.mp4`

---

## 📚 Playlist Download

Choose:
- 🌍 Full playlist  
- ☝️ Selected items (example: `1,4,7`)

Output structure:
```
Playlist Name/
 ├── 01 - Title.mp4
 ├── 02 - Title.mp4
```

---

## 📄 Batch Download using `url.txt`

### 1️⃣ Create file
```
url.txt
```

### 2️⃣ Add URLs (one per line)
```
https://youtube.com/...
https://youtube.com/...
```

### 3️⃣ Choose **Option 4** from menu

---

## ❌ Common Errors & Fixes

### ❌ FFmpeg not found
✅ Solution:
- Install FFmpeg
- Restart terminal

### ❌ Permission denied (Termux)
```bash
termux-setup-storage
```

---

## ❤️ Credits

```
≈☆ Made with 💖 by Genius 💞 ☆≈
```

Backend powered by **yt-dlp**


## 📸 Screenshots

### 🎛️ Main Menu
<p align="center">
  <img src="Main Menu.jpg" width="600">
</p>

### 🎵 Song Download
<p align="center">
  <img src="Song Download.jpg" width="600">
</p>

### 🎬 Video Download
<p align="center">
  <img src="Video Download.jpg" width="600">
</p>

### 📚 Playlist Download
<p align="center">
  <img src="Playlist Download.jpg" width="600">
</p>
