# Soundcloud-To-iTunes
Automaticly download songs, albums, and playlists from soundcloud and add them to your iTunes library. Meta data tags such as artist, album, title, and album artwork will all be added automaticly.

# Requirements
- selenium
- eyed3
- requests
- platform
- os

To download all required packages, use `$ pip install -r requirements.txt`

This program comes with Chromedriver for chrome version 87. If you are getting errors to do with chrome version, go to [ChromeDriver's Downloads Page](https://chromedriver.chromium.org/downloads) and replace `chromedriver.exe` with the one for your chrome version

# Usage
1. Download the repo by using `$ git clone https://github.com/sebastianrich18/Soundcloud-To-iTunes/` in the terminal
2. Move into the newly downloaded folder by using `$ cd Soundcloud-To-iTunes`
3. Run the program by using `$ python3 soundcloud-to-iTunes.py`
  - If you get any errors, try using `$ pip install -r requirements.txt` to install all required packages
4. Paste the link to the song, album, or playlist you want to download and press enter
5. Check iTunes to make sure all songs were transfered properly

# If album art doesnt show up in iTunes
- Right click on the song or album in iTunes and click `Album Info`
- Click on the `Artwork` tab then click `Add Artwork`
- Navigate to where you downloaded the repo and go into the `songs` folder and click `art.jpg`
