#!/bin/bash
current_dir="$PWD"

cd "$current_dir"/tool/back
gnome-terminal -- python3 server.py
sleep 40
cd "$current_dir"/tool
gnome-terminal -- npm start

