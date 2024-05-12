#!/bin/bash

cd ~/tool/back
gnome-terminal -- python3 server.py
sleep 60
cd ~/tool
gnome-terminal -- npm start

