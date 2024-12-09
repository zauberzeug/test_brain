#!/bin/bash

# Check if script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (sudo)"
    exit 1
fi

# Create service file
cat > /etc/systemd/system/write-datetime.service << EOL
[Unit]
Description=Write Current Date and Time to Home Directory
After=network.target

[Service]
Type=simple
ExecStart=/home/zauberzeug/test_brain/rtc_test/time.sh
User=zauberzeug
Environment="HOME=/home/zauberzeug"

[Install]
WantedBy=multi-user.target
EOL

# Create timer file
cat > /etc/systemd/system/write-datetime.timer << EOL
[Unit]
Description=Run write-datetime.service 30 seconds after boot

[Timer]
OnBootSec=30
Unit=write-datetime.service

[Install]
WantedBy=timers.target
EOL

# Make time.sh executable
chmod +x /home/zauberzeug/test_brain/rtc_test/time.sh

# Reload systemd, enable and start timer
systemctl daemon-reload
systemctl enable write-datetime.timer
systemctl start write-datetime.timer

# Verify setup
echo "Checking service status..."
systemctl status write-datetime.service
echo "Checking timer status..."
systemctl status write-datetime.timer

echo "Setup complete! The script will run 30 seconds after each boot."
