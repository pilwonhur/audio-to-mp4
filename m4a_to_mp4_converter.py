#!/usr/bin/env python3
"""
M4A/MP3 to MP4 Converter
Converts audio files (.m4a, .mp3) to MP4 with a blank video track for YouTube upload.

Usage:
    python m4a_to_mp4_converter.py <input_file> [<input_file2> ...]

Requirements:
    - Python 3.8+
    - FFmpeg installed and available in PATH
"""

import subprocess
import sys
import os
from pathlib import Path


def check_ffmpeg():
    """Check if FFmpeg is installed and available."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def convert_audio_to_mp4(input_path: str) -> tuple[bool, str]:
    """
    Convert an audio file to MP4 with a blank video track.
    
    Args:
        input_path: Path to the input audio file (.m4a or .mp3)
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    input_file = Path(input_path)
    
    # Validate input file exists
    if not input_file.exists():
        return False, f"Input file not found: {input_path}"
    
    # Validate file extension
    if input_file.suffix.lower() not in ['.m4a', '.mp3']:
        return False, f"Unsupported file format: {input_file.suffix}. Only .m4a and .mp3 are supported."
    
    # Create output path (same directory, .mp4 extension)
    output_file = input_file.with_suffix('.mp4')
    
    # Check if output already exists
    if output_file.exists():
        # Add timestamp to avoid overwriting
        timestamp = input_file.stat().st_mtime
        output_file = input_file.with_stem(f"{input_file.stem}_{int(timestamp)}").with_suffix('.mp4')
    
    try:
        # FFmpeg command to create MP4 with blank video
        # -f lavfi -i color=c=black:s=1920x1080:r=1 : Create a black video (1fps to minimize size)
        # -i <audio> : Input audio file
        # -c:v libx264 : Video codec
        # -tune stillimage : Optimize for still image (reduces size)
        # -c:a aac : Audio codec (AAC for compatibility)
        # -b:a 192k : Audio bitrate
        # -shortest : Match video length to audio length
        # -pix_fmt yuv420p : Pixel format for compatibility
        
        cmd = [
            "ffmpeg",
            "-y",  # Overwrite output file if exists
            "-f", "lavfi",
            "-i", "color=c=black:s=1920x1080:r=1",  # Black video, 1920x1080, 1 fps
            "-i", str(input_file),
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            "-pix_fmt", "yuv420p",
            str(output_file)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        return True, f"Successfully converted: {output_file.name}"
        
    except subprocess.CalledProcessError as e:
        return False, f"FFmpeg error: {e.stderr}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    """Main entry point for the converter."""
    if len(sys.argv) < 2:
        print("Usage: python m4a_to_mp4_converter.py <input_file> [<input_file2> ...]")
        print("Supported formats: .m4a, .mp3")
        sys.exit(1)
    
    # Check FFmpeg availability
    if not check_ffmpeg():
        print("Error: FFmpeg is not installed or not in PATH.")
        print("Please install FFmpeg: brew install ffmpeg")
        sys.exit(1)
    
    # Process each input file
    input_files = sys.argv[1:]
    success_count = 0
    error_count = 0
    
    for input_file in input_files:
        success, message = convert_audio_to_mp4(input_file)
        print(message)
        
        if success:
            success_count += 1
        else:
            error_count += 1
    
    # Summary for batch processing
    if len(input_files) > 1:
        print(f"\nSummary: {success_count} succeeded, {error_count} failed")
    
    sys.exit(0 if error_count == 0 else 1)


if __name__ == "__main__":
    main()
