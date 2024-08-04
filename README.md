![ClipTrickster](ClipTrickster.png)
## ClipTrickster
It is a multi-functional clipboard monitoring and modification tool that runs in the background, saving, modifying, or destroying copied content for increased security and privacy.
Running in normal mode or silently in the background, ClipTrickster offers three primary modes of operation: monitoring, modifying, and destroying clipboard content. Whether you need to log your copied content with timestamps, introduce random modifications, or ensure nothing remains in the clipboard, ClipTrickster has you covered.

## Features
- Clipboard Monitoring: Constantly monitors clipboard activity, saving copied content with structured timestamps for easy tracking and reference.
- Clipboard Modification: Automatically adds random characters to clipboard content, ensuring data integrity is disrupted and enhancing security.
- Clipboard Destruction: Clears the clipboard continuously, preventing any copied data from being used or retrieved.
- Silent and Normal Modes: Choose between silent operation, which hides all activities and logs, and normal mode, which provides user-friendly prompts and visibility.

## Installation
```bash
git clone https://github.com/raikoho/ClipTrickster.git
cd ClipTrickster
pip install -r requirements.txt
python cliptrickster.py
```

## Configuration
Edit the config.txt file to choose your desired module and activity mode:
```bash
module: monitor
activity: normal

//* Below For comments and mini instruction
//* module: monitor / modify / destroy
//* activity: normal / silence
//* end of config.txt
```

## Contact
For any questions or issues, please open an issue on GitHub or contact the project maintainer at https://www.linkedin.com/in/bohdan-misyonh/
