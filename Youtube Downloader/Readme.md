[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# YouTube Download Script
The python script can download both video and audio files from YouTube

What the program does?
- Download video,audio files from YouTube
- Accepts multiple URL(s) at the same time
- Can specify where to store the files
- Can download videos in there the highest resolution available
- Saves audio files in ".mp3" format

### Requirements
> Python 3
> 
> pip install -r requirements.txt

### Usage
```
ytavdownload.py [-h] -u URLS [URLS ...] [-a] [-v] [-p PATH] [-k] [-hd]

DOWNLOAD AUDIO AND VIDEO FILES FROM YOUTUBE

optional arguments:
  -h, --help          show this help message and exit
  -u URLS [URLS ...]  URLS To Download From
  -a                  Download Audio File
  -v                  Download Video File
  -p PATH             Path For To Store The Files
  -k                  Keep The Video With The Audio File
  -hd                 Download The HD Video

```


