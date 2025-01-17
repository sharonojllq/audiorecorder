# AudioRecorder

## Overview

AudioRecorder is a simple Python-based tool for Windows that allows users to record, edit, and save audio files. This program leverages the `sounddevice` library to manage audio input and output operations and the `wave` library to handle audio file operations.

## Features

- Record audio from your default microphone.
- Playback recorded audio.
- Save the recorded audio to a WAV file.
- Delete the recorded audio from memory.

## Requirements

- Python 3.x
- `sounddevice` library
- `numpy` library

## Installation

1. Make sure you have Python 3.x installed on your Windows machine.
2. Install the required libraries using pip:

   ```bash
   pip install sounddevice numpy
   ```

3. Download the `AudioRecorder.py` file to your local machine.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `AudioRecorder.py` is located.
3. Run the script using Python:

   ```bash
   python AudioRecorder.py
   ```

4. Follow the on-screen prompts to record, play, save, or delete audio.

## Notes

- The default audio duration is set to 5 seconds. You can modify this in the `AudioRecorder` class initialization.
- The default output file is `output.wav`. You can change this by providing a different filename when initializing the `AudioRecorder` class.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- This tool uses the `sounddevice` library for audio recording and playback.
- `numpy` and `wave` are used for handling the audio data and file operations.