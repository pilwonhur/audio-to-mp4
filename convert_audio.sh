#!/bin/bash
# Convert Audio to MP4 - Shell wrapper for Automator Quick Action
# This script is called by the Automator Quick Action workflow

# Get the directory of this script (to find the Python converter)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/m4a_to_mp4_converter.py"

# Check if Python script exists
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    osascript -e 'display notification "Python converter script not found" with title "Convert Audio to MP4" subtitle "Error"'
    exit 1
fi

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    osascript -e 'display notification "FFmpeg is not installed. Run: brew install ffmpeg" with title "Convert Audio to MP4" subtitle "Error"'
    exit 1
fi

# Process each input file
SUCCESS_COUNT=0
ERROR_COUNT=0
TOTAL_FILES=$#

for file in "$@"; do
    if python3 "$PYTHON_SCRIPT" "$file"; then
        ((SUCCESS_COUNT++))
    else
        ((ERROR_COUNT++))
    fi
done

# Display notification with results
if [[ $ERROR_COUNT -eq 0 ]]; then
    if [[ $TOTAL_FILES -eq 1 ]]; then
        osascript -e 'display notification "Conversion completed successfully" with title "Convert Audio to MP4" sound name "Glass"'
    else
        osascript -e "display notification \"$SUCCESS_COUNT files converted successfully\" with title \"Convert Audio to MP4\" sound name \"Glass\""
    fi
else
    if [[ $TOTAL_FILES -eq 1 ]]; then
        osascript -e 'display notification "Conversion failed" with title "Convert Audio to MP4" subtitle "Error" sound name "Basso"'
    else
        osascript -e "display notification \"$SUCCESS_COUNT succeeded, $ERROR_COUNT failed\" with title \"Convert Audio to MP4\" subtitle \"Partial Success\" sound name \"Basso\""
    fi
fi

exit 0
