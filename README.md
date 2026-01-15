# M4A/MP3 to MP4 Converter

Convert audio files (.m4a, .mp3) to MP4 with a blank video track for YouTube upload using a macOS Quick Action.

## Requirements

- **macOS** Monterey (12.0) or later
- **Python** 3.8+
- **FFmpeg** - Install via Homebrew:
  ```bash
  brew install ffmpeg
  ```

## Installation

### Quick Install (Recommended)
```bash
cp -r "Convert Audio to MP4.workflow" ~/Library/Services/
```

### Manual Install
1. Double-click `Convert Audio to MP4.workflow`
2. Click "Install" when prompted

## Usage

### Via Quick Action (Right-Click Menu)
1. In Finder, right-click on an `.m4a` or `.mp3` file
2. Select **Quick Actions** → **Convert Audio to MP4**
3. Wait for the notification confirming conversion
4. The `.mp4` file will appear in the same folder

### Via Terminal
```bash
python3 m4a_to_mp4_converter.py <input_file.m4a>
```

**Batch processing:**
```bash
python3 m4a_to_mp4_converter.py file1.m4a file2.mp3 file3.m4a
```

## Files

| File | Description |
|------|-------------|
| `m4a_to_mp4_converter.py` | Python script that performs the conversion |
| `convert_audio.sh` | Shell wrapper with notifications |
| `Convert Audio to MP4.workflow/` | Automator Quick Action |

## Troubleshooting

**Quick Action not appearing?**
1. Go to **System Preferences** → **Extensions** → **Finder**
2. Ensure "Convert Audio to MP4" is checked
3. Restart Finder: `killall Finder`

**FFmpeg not found?**
```bash
brew install ffmpeg
```

**Permission denied?**
```bash
chmod +x m4a_to_mp4_converter.py convert_audio.sh
```

## License

MIT License
