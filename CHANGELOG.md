# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-05-02
### Added
- **OGG format support**: Added `.ogg` (Ogg Vorbis) as a supported input audio format across the Python converter, shell wrapper, Automator workflow, and all documentation.

## [1.0.1] - 2026-02-28
### Fixed
- **macOS 15 Sequoia Compatibility**: Fixed the Automator Quick Action failing silently after Apple completely removed the built-in Python 3 installation at `/usr/bin/python3`.
- Updated Automator workflow (`document.wflow`) and shell wrapper (`convert_audio.sh`) to use `python3` via the system `PATH` (e.g., from Homebrew or Xcode Command Line Tools) instead of using a hardcoded absolute path.

## [1.0.0] - 2026-01-15
### Added
- Initial release of the "Convert Audio to MP4" macOS Quick Action.
- Core python converter (`m4a_to_mp4_converter.py`) utilizing FFmpeg to generate blank video tracks.
- Automator workflow and shell script wrapper integration for Finder right-click context menu.
- Notifications for successful and failed conversions via macOS Notification Center.
