# YouTube Extractor

<p align="center">
    <img src="assets/images/Logo.JPG" alt="Logo" border="0">
    <br>A Simple and Easy to use GUI based YouTube Video/Audio Extractor.
</p>

---

## Motivation

We all have tried downloading a YouTube video atleast once in our lives. Be it a song or a video for your school/college assignment. <br>
True, there are plenty of browser extensions and online websites avilable to download YouTube videos. But, at times either the extension malfunctions or the servers don't work anymore. 

And hence YouTube-Extractor was made. You can launch it any time and download any video/audio on YouTube.

## Usage

Typing-Speed-Test uses custom fonts. Most windows computers have them preinstalled. However, if you don't have them already, just open the `Fonts` folder present in assets and launch all the files present and hit on install.

Before running the YouTube-Extractor, make sure you have pytube3 installed. To do this, type the following code in your terminal.
<pre>
pip install pytube3
</pre>

As an alternative you can also cd to YouTube-Extractor directory and type 
<pre>
pip install -r requirements.txt
</pre>

To check if pytube3 is successfully installed on your computer, open your terminal and type `pytube3 --version`
Once you have pytube3 installed, just run the `YouTube Extractor.py` file present in the `src` folder.

**NOTE** : Sometimes, the application might throw an error stating that the video is not avilable. Just close the window and launch the program again.

**NOTE** : If you are facing a `KeyError: 'cipher'`, you might have to modify your pytube3 package files.<br>
Just follow the steps below : <br>
- Open your terminal and type pip show pytube3
- Open your file explorer and go to the location it shows (Default = c:\users\username\appdata\local\programs\python\python37\lib\site-packages)
- Open the `extract.py` file present in the `pytube` folder.
- Go to line number **306** or search for `parse_qs(formats[i]["cipher"])`
- Change "cipher" to "signatureCipher" (make sure 'C' is capital).