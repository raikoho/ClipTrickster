![ClipTrickster](ClipTrickster.png)
## ClipTrickster
It is a multi-functional clipboard monitoring and modification tool that runs in the background, saving, modifying, or destroying copied content for increased security and privacy.
Running in normal mode or silently in the background, ClipTrickster offers three primary modes of operation: monitoring, modifying, and destroying clipboard content. ClipTrickster designed to take full control and take control of the clipboard hostage.

## Features
- Monitor: Constantly monitors clipboard activity, saving copied content with structured timestamps for easy tracking and reference. Complete copy history.
- Modify: Automatically adds random characters to clipboard content, ensuring data integrity is disrupted and enhancing security. Makes every copy wrong and inaccurate.
- Destroy: Clears the clipboard continuously, preventing any copied data from being used or retrieved. Makes it impossible to use any copying.
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
That is, you can set one of 3 modules in "module:" and one of 2 activity in "activity:" in accordance:
1) monitor / modify / destroy  
2) normal / silence

## Contact
For any questions or issues, please open an issue on GitHub or contact the project maintainer at https://www.linkedin.com/in/bohdan-misyonh/
