# 🎵 Audio to MP4 Converter

> Convert M4A/MP3 audio files to MP4 with a blank video track for YouTube upload — right from Finder's context menu.

[![macOS](https://img.shields.io/badge/macOS-12.0%2B-blue?logo=apple)](https://www.apple.com/macos/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Problem

YouTube doesn't accept audio-only files (.m4a, .mp3) for upload. You need to convert them to video format first — but running terminal commands for every file is tedious.

## ✨ Solution

A **macOS Quick Action** that lets you right-click any audio file and instantly convert it to MP4 with a black video track, ready for YouTube.

![Demo](assets/demo.gif) <!-- Optional: Add a demo GIF -->

## 📦 Features

- ✅ **One-click conversion** from Finder's right-click menu
- ✅ **Supports M4A and MP3** audio formats
- ✅ **Batch processing** — select multiple files at once
- ✅ **Native notifications** for success/failure feedback
- ✅ **1080p black video** with optimized encoding (minimal file size)
- ✅ **No quality loss** — audio is re-encoded at 192kbps AAC

## 🔧 Requirements

| Requirement | Version | Installation |
|-------------|---------|--------------|
| macOS | Monterey 12.0+ | — |
| Python | 3.8+ | Pre-installed on macOS |
| FFmpeg | Latest | `brew install ffmpeg` |

## 🚀 Installation

### 1. Install FFmpeg (if not already installed)

```bash
brew install ffmpeg
```

### 2. Clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/audio-to-mp4.git
cd audio-to-mp4
```

### 3. Install the Quick Action

```bash
cp -r "Convert Audio to MP4.workflow" ~/Library/Services/
```

### 4. Refresh services (or log out and back in)

```bash
/System/Library/CoreServices/pbs -update
killall Finder
```

### 5. Enable the extension (if needed)

1. Open **System Settings**
2. Go to **General** → **Login Items & Extensions**
3. Scroll to **Finder Extensions**
4. Enable **Convert Audio to MP4**

## 📖 Usage

### Via Quick Action (Recommended)

1. **Right-click** any `.m4a` or `.mp3` file in Finder
2. Select **Services** → **Convert Audio to MP4**
3. Wait for the notification confirming completion
4. The `.mp4` file appears in the same folder

### Via Terminal

**Single file:**
```bash
python3 m4a_to_mp4_converter.py song.m4a
```

**Multiple files:**
```bash
python3 m4a_to_mp4_converter.py track1.m4a track2.mp3 track3.m4a
```

## 📁 Project Structure

```
audio-to-mp4/
├── m4a_to_mp4_converter.py      # Core Python converter script
├── convert_audio.sh              # Shell wrapper with notifications
├── Convert Audio to MP4.workflow/  # Automator Quick Action
│   └── Contents/
│       ├── document.wflow        # Workflow definition
│       └── Info.plist            # Service configuration
├── README.md                     # This file
├── PRD.md                        # Product Requirements Document
└── LICENSE                       # MIT License
```

## ⚙️ How It Works

1. **Quick Action** intercepts the right-click on audio files
2. **Shell script** validates dependencies and calls the Python converter
3. **Python script** uses FFmpeg to:
   - Generate a 1920×1080 black video at 1 fps (minimal size)
   - Mux the audio track with the video
   - Output an `.mp4` file with `libx264` video and `AAC` audio
4. **macOS notification** reports success or failure

### FFmpeg Command Used

```bash
ffmpeg -y \
  -f lavfi -i "color=c=black:s=1920x1080:r=1" \
  -i input.m4a \
  -c:v libx264 -tune stillimage \
  -c:a aac -b:a 192k \
  -shortest -pix_fmt yuv420p \
  output.mp4
```

## 🔍 Troubleshooting

### Quick Action not appearing in menu

```bash
# Refresh the services database
/System/Library/CoreServices/pbs -update
killall Finder
```

Then enable it in **System Settings** → **General** → **Login Items & Extensions** → **Finder Extensions**.

### "FFmpeg not found" error

```bash
# Install FFmpeg via Homebrew
brew install ffmpeg

# Verify installation
ffmpeg -version
```

### "Service input error"

This usually means the workflow wasn't installed correctly. Reinstall:

```bash
rm -rf ~/Library/Services/"Convert Audio to MP4.workflow"
cp -r "Convert Audio to MP4.workflow" ~/Library/Services/
killall Finder
```

### Permission denied

```bash
chmod +x m4a_to_mp4_converter.py convert_audio.sh
```

## 🛠️ Customization

### Change video resolution

Edit `m4a_to_mp4_converter.py` line 72:
```python
"-i", "color=c=black:s=1280x720:r=1",  # Change to 720p
```

### Change audio bitrate

Edit `m4a_to_mp4_converter.py` line 76:
```python
"-b:a", "320k",  # Higher quality audio
```

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📬 Author

**Pilwon Hur**

---

<p align="center">
  Made with ❤️ for content creators who need to upload audio to YouTube
</p>
