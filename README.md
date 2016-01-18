```
usage: python itunes-check.py [-h] path

This script prints the names of any media file ffmpeg deems corrupt to stdout.

positional arguments:
  path        A file or directory referencing media files to check
```

Dependencies
-----------------
Requires Python 2.7.
Requires `ffmpeg` be installed and available as a shell command.

Expected Runtime
-----------------
Took 1.5 hours when run against my iTunes library of over 8,000 songs.
My iTunes library is stored on a commodity USB Flash drive.

Bugs / Notes
-----------------
- The lack of progress reporting is pretty terrible.
- Most audio files found were not playable by iTunes, but some were (these files had corruptions in their album art).
- I have no idea if the parallelism helps or hurts performance. I assumed ffmpeg was CPU-intensive, but I have not confiremed this.
