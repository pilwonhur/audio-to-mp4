# PRD_init.md

## Description
- I have a python script `m4a_to_mp4_converter.py` that converts m4a files to mp4 files with blank video track.
- I need this conversion since youtube does not support m4a files.
- Here is the uage of the script:
```bash
python m4a_to_mp4_converter.py <input_m4a_file>
```

## Requirements
- Intead of typing the command from the terminal, I want to use the quick action to convert m4a or mp3 files to mp4 files with blank video track.
- The quick action can be selected when I right-click an m4a or mp3 file from a Finder.
- Then, the quick action should run the python script with the selected file as an argument.
