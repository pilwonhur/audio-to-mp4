# Product Requirements Document (PRD)
## M4A/MP3/OGG to MP4 Converter Quick Action

**Version:** 1.0  
**Date:** 2026-01-15  
**Author:** Pilwon Hur

---

## 1. Overview

### 1.1 Problem Statement
YouTube does not support direct upload of audio-only files such as `.m4a`, `.mp3`, or `.ogg`. Currently, the conversion from audio to video with a blank video track requires executing a Python script (`m4a_to_mp4_converter.py`) manually from the terminal, which is inconvenient for frequent use.

### 1.2 Solution
Create a macOS Quick Action (Automator workflow) that integrates with Finder's right-click context menu, enabling one-click conversion of `.m4a`, `.mp3`, and `.ogg` files to `.mp4` format with a blank video track.

### 1.3 Target Platform
- **OS:** macOS (Monterey 12.0+)
- **Integration:** Finder Quick Actions

---

## 2. Goals & Success Metrics

| Goal | Success Metric |
|------|----------------|
| Simplify audio-to-video conversion | Reduce conversion from 3+ steps (open terminal, navigate, run command) to 1 step (right-click → convert) |
| Support multiple audio formats | Accept `.m4a`, `.mp3`, and `.ogg` file types |
| Seamless user experience | Output file saved in the same directory as input |
| Reliability | 100% of valid audio files convert successfully |

---

## 3. Functional Requirements

### 3.1 Quick Action Integration
- **FR-01:** The Quick Action shall appear in Finder's right-click context menu when selecting `.m4a`, `.mp3`, or `.ogg` files
- **FR-02:** The Quick Action shall support single file selection
- **FR-03:** The Quick Action shall support batch processing (multiple file selection)

### 3.2 Conversion Process
- **FR-04:** The system shall invoke the existing `m4a_to_mp4_converter.py` script with the selected file(s) as argument(s)
- **FR-05:** The output `.mp4` file shall be saved in the same directory as the source file
- **FR-06:** The output filename shall match the input filename with `.mp4` extension

### 3.3 User Feedback
- **FR-07:** The system shall display a notification upon successful conversion
- **FR-08:** The system shall display an error notification if conversion fails

---

## 4. Non-Functional Requirements

- **NFR-01:** Conversion shall complete within 30 seconds for files under 100MB
- **NFR-02:** The Quick Action shall work offline (no internet required)
- **NFR-03:** The workflow shall be compatible with macOS Monterey (12.0) and later
- **NFR-04:** Installation shall require no additional user configuration

---

## 5. Technical Specifications

### 5.1 Dependencies
| Component | Requirement |
|-----------|-------------|
| Python | 3.8+ |
| FFmpeg | Required by converter script |
| macOS Automator | Built-in |

### 5.2 Implementation Approach
1. **Automator Workflow:** Create a "Quick Action" workflow in Automator
2. **File Type Filter:** Configure to receive `.m4a`, `.mp3`, and `.ogg` files from Finder
3. **Shell Script Action:** Execute the Python script with passed file paths
4. **Notification:** Use `osascript` to display completion/error notifications

### 5.3 File Structure
```
~/Library/Services/
└── Convert Audio to MP4.workflow
    └── Contents/
        └── document.wflow
```

---

## 6. User Stories

| ID | Story | Priority |
|----|-------|----------|
| US-01 | As a content creator, I want to right-click an m4a file and convert it to mp4 so I can upload to YouTube | High |
| US-02 | As a user, I want to convert multiple audio files at once to save time | Medium |
| US-03 | As a user, I want to receive a notification when conversion completes so I know when to upload | Medium |

---

## 7. Out of Scope

- Custom video background (only blank/black video track)
- Audio quality adjustment during conversion
- Drag-and-drop conversion interface
- Windows/Linux support

---

## 8. Implementation Phases

### Phase 1: Core Functionality (MVP)
- [ ] Create Automator Quick Action workflow
- [ ] Configure file type filters for .m4a, .mp3, and .ogg
- [ ] Integrate shell script to call Python converter
- [ ] Test single file conversion

### Phase 2: Enhanced UX
- [ ] Add success/error notifications
- [ ] Support batch file conversion
- [ ] Add progress indicator for large files

### Phase 3: Documentation
- [ ] Write installation instructions
- [ ] Create user guide
- [ ] Document troubleshooting steps

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Python not in PATH | Quick Action fails silently | Use absolute Python path or check PATH in script |
| FFmpeg not installed | Conversion fails | Add dependency check with helpful error message |
| Large file timeout | User thinks conversion failed | Add progress notification or longer timeout |

---

## 10. Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2026-01-15 | Initial draft (PRD_init.md) | Pilwon Hur |
| 1.0 | 2026-01-15 | Refined PRD with detailed requirements, specs, and phases | Pilwon Hur |
| 1.0.1 | 2026-02-28 | Fixed hardcoded Python path issue for macOS Sequoia compatibility | Pilwon Hur |
