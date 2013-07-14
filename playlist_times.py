#!/usr/bin/env python
import sys
import optparse
from datetime import datetime, timedelta
from mutagen.mp3 import MP3
from mutagen.m4a import M4A
from mutagen.easyid3 import EasyID3

p = optparse.OptionParser()
p.add_option('--inputfile', '-i')
p.add_option('--starttime', '-s')
p.add_option('--filter', '-f', default=None)
options, arguments = p.parse_args()

filename = options.inputfile
raw_starttime = options.starttime
filt = options.filter

if not filename:
    p.print_help()
else:
    current_time = datetime.strptime(raw_starttime, '%H:%M')

    with file(filename, 'rU') as f:
        line = f.readline()
        while line:
            if line and line.startswith('/'):
                song_file_name = line.strip('\n').strip('\r').lower()
                if song_file_name.endswith('.mp3'):
                    audio = MP3(song_file_name, ID3=EasyID3)
                elif song_file_name.endswith('.m4a'):
                    audio = M4A(song_file_name)
                else:
                    raise Exception("unrecgonised format for :" + song_file_name)

                duration = audio.info.length
                title = audio.tags.get('title')
                if title:
                    title = title[0]
                artist = audio.tags.get('artist')
                if artist:
                    artist = artist[0]

                if not filt or filt in (artist or '') or filt in (title or '') or filt in (song_file_name or ''):
                    print u'{time}: {artist}-{title}'.format(time=current_time.strftime('%H:%M'),
                             artist=artist or song_file_name, title=title or '')
                    current_time += timedelta(seconds=duration)

            line = f.readline()
