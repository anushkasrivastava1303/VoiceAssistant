# Voice Assistant

A Python-based **Voice Assistant** that can recognize speech and respond to simple voice commands. This project uses popular libraries like **SpeechRecognition** and **pyttsx3** to create a basic interactive assistant capable of performing various tasks such as setting alarms, providing weather updates, and delivering predefined responses.

## Features
- **Speech Recognition**: Converts spoken words into text using the **SpeechRecognition** library.
- **Text-to-Speech**: Uses **pyttsx3** to convert text responses into speech, providing a voice output.
- **Basic Commands**: Capable of responding to voice commands for tasks such as:
  - Setting alarms
  - Providing weather updates
  - Answering predefined queries
- **Extensible**: The project is designed in a way that allows you to easily add new commands and extend the assistant's capabilities.


## Installation

### Prerequisites
- Python 3.x
- Libraries: You can install the necessary libraries using the `requirements.txt` file.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/anushkasrivastava1303/VoiceAssistant.git
   cd VoiceAssistant
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the **voice assistant**:
   ```bash
   python assistant.py
   ```

## Usage
1. Once the assistant starts running, speak into your microphone.
2. The assistant will convert your speech to text and perform an action based on the command.
3. For example, you can say:
   - "Set an alarm for 7 AM"
   - "What's the weather today?"
   - "Tell me a joke"

## Technologies Used
- **Python**: The core programming language used for the project.
- **SpeechRecognition**: A Python library for performing speech recognition, used to convert speech into text.
- **pyttsx3**: A Python library for converting text to speech, used for generating spoken responses.
- **OpenWeatherMap API**: (Optional) Used to provide weather updates by fetching live weather data.

## Project Structure
```
VoiceAssistant/
├── assistant.py         # Main script that runs the voice assistant
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── utils.py             # Utility functions (e.g., weather fetch, command parsing)
```

## Future Improvements
- Integrate more advanced NLP capabilities for understanding complex sentences.
- Add support for executing system-level commands (e.g., opening applications).
- Improve error handling and responses for unrecognized commands.
- Expand the range of supported commands (e.g., setting timers, reminders, etc.).
- Integrate with additional APIs (e.g., Google Calendar for scheduling).

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you want to help improve the voice assistant.
