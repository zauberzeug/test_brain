#!/bin/bash

# Name der Systemd-Unit
UNIT_NAME="hwclock-rtc0.service"
UNIT_PATH="/etc/systemd/system/$UNIT_NAME"

echo "Stoppe die Systemd-Unit $UNIT_NAME..."
sudo systemctl stop $UNIT_NAME || true

echo "Deaktiviere die Systemd-Unit $UNIT_NAME..."
sudo systemctl disable $UNIT_NAME || true

if [[ -f "$UNIT_PATH" ]]; then
    echo "Entferne die Systemd-Unit-Datei..."
    sudo rm "$UNIT_PATH"
    echo "Die Systemd-Unit-Datei wurde entfernt."
else
    echo "Die Systemd-Unit-Datei existiert nicht."
fi

echo "Lade Systemd-Dienste neu..."
sudo systemctl daemon-reload

echo "Die Systemd-Unit $UNIT_NAME wurde erfolgreich entfernt."
