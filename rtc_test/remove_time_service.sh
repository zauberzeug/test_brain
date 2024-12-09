#!/bin/bash

# Check if script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (sudo)"
    exit 1
fi

# Stop and disable the timer
echo "Stopping and disabling timer..."
systemctl stop write-datetime.timer
systemctl disable write-datetime.timer

# Stop and disable the service
echo "Stopping and disabling service..."
systemctl stop write-datetime.service
systemctl disable write-datetime.service

# Remove service and timer files
echo "Removing service and timer files..."
rm -f /etc/systemd/system/write-datetime.service
rm -f /etc/systemd/system/write-datetime.timer

# Reload systemd to apply changes
echo "Reloading systemd..."
systemctl daemon-reload

# Optional: Remove the datetime.txt file
read -p "Do you want to remove the datetime.txt file? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    rm -f /home/zauberzeug/datetime.txt
    echo "datetime.txt removed."
fi

echo "Cleanup complete! All service components have been removed."
