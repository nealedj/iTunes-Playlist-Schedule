iTunes Playlist Schedule
=============

A quick script to output the times at which tracks on an exported iTunes playlist will begin given a start time

* Export the iTunes playlist as .m3u8 (not XML as this does not preserve playlist order)
* Run the script to output the times:
  * python playlist_times.py -i MyPlaylist.m3u8 -s 19:00

Dependencies
-------

* mutagen

Usage
-------

Usage: playlist_times.py [options]

Options:

  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile=INPUTFILE
  -s STARTTIME, --starttime=STARTTIME
  -f FILTER, --filter=FILTER

Filter outputs only tracks which contain the string passed in the -f argument