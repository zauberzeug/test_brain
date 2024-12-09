#!/bin/bash

# This script appends the current date and time to a file in the home directory to check if the RTC is working correctly.
# It is intended to be executed automatically 30 seconds after system boot using systemd.

# Get the current date and time
current_datetime=$(date +"%Y-%m-%d %H:%M:%S")

# Specify the file name
file_name="$HOME/datetime.txt"

# Get Unix timestamp
unix_time=$(date +%s)
# Write Unix timestamp to file
echo "Unix Timestamp: $unix_time" >> "$file_name"

# Write the date and time to the file
echo "Current Date and Time: $current_datetime" >> "$file_name"

echo "The current date and time have been written to $file_name."



# ============================
# SETUP INSTRUCTIONS FOR AUTOSTART USING SYSTEMD
# ============================

# 1. Create a systemd service file to manage the execution of this script:
#    sudo vi /etc/systemd/system/write-datetime.service

# 2. Add the following content to the service file:
# [Unit]
# Description=Write Current Date and Time to Home Directory
# After=network.target

# [Service]
# Type=simple
# ExecStart=/home/zauberzeug/test_brain/time.sh
# User=zauberzeug
# Environment="HOME=/home/zauberzeug"

# [Install]
# WantedBy=multi-user.target

# 3. Create a systemd timer file to trigger the service 30 seconds after boot:
#    sudo vi /etc/systemd/system/write-datetime.timer

# 4. Add the following content to the timer file:
# [Unit]
# Description=Run write-datetime.service 30 seconds after boot

# [Timer]
# OnBootSec=30
# Unit=write-datetime.service

# [Install]
# WantedBy=timers.target

# 5. Enable and start the timer to activate it at boot:
#    sudo systemctl daemon-reload
#    sudo systemctl enable write-datetime.timer
#    sudo systemctl start write-datetime.timer

# 6. Verify the setup:
#    Check the status of the timer:
#    systemctl status write-datetime.timer
#
#    Check the status and logs of the service to confirm it runs successfully:
#    systemctl status write-datetime.service
#    journalctl -u write-datetime.service

# By following these steps, the script will automatically run 30 seconds after boot and append the date and time to /home/zauberzeug/datetime.txt.
