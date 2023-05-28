# First clone and install codec2 from github


# ets cmds:
cat /etc/os-release
uname -r

ls *.raw
ls *.bit

# Record, or record and convert to 8000 (because my mic runs at 44100 but at 8000 the quality is way better)
arecord -D hw:3,0 -f S16_LE -r 44100 -d 6 podcast.raw
arecord -D hw:3,0 -f S16_LE -r 44100 -d 6 -t raw | sox -t raw -r 44100 -e signed -b 16 -c 1 - -r 8000 podcast.raw


# encode audio recording with codec2
./codec2/build_linux/src/c2enc 3200 podcast.raw mypodcast_c2.bit

# -- Start server on WSL--
With basic python

# Start client on Rpi to send file
python3 src/file_send.py mypodcast_c2.bit


# On WSL side decode the received file

./build_linux/src/c2dec 3200 mypodcast_c2.bit reveicedPod.raw
aplay reveicedPod.raw
