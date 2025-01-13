#!/bin/bash

# Name der Systemd-Unit
UNIT_NAME="hwclock-rtc0.service"
UNIT_PATH="/etc/systemd/system/$UNIT_NAME"

echo "Erstelle die Systemd-Unit: $UNIT_NAME..."

# Prüfen, ob die Datei bereits existiert
if [[ -f "$UNIT_PATH" ]]; then
    echo "Die Systemd-Unit $UNIT_NAME existiert bereits. Überspringe das Erstellen."
else
    # Systemd-Unit erstellen
    cat <<EOL | sudo tee $UNIT_PATH > /dev/null
[Unit]
Description=Set system clock from RTC0
DefaultDependencies=no
Before=time-sync.target

[Service]
Type=oneshot
ExecStart=/sbin/hwclock --hctosys

[Install]
WantedBy=sysinit.target
EOL
    echo "Die Systemd-Unit wurde erstellt unter $UNIT_PATH."
fi

# Systemd-Dienste neu laden
echo "Lade Systemd-Dienste neu..."
sudo systemctl daemon-reload

# Aktivieren der Unit, damit sie beim Booten startet
echo "Aktiviere die Systemd-Unit $UNIT_NAME..."
sudo systemctl enable $UNIT_NAME

# Testen der Unit
echo "Starte die Systemd-Unit $UNIT_NAME..."
sudo systemctl start $UNIT_NAME

# Status der Unit überprüfen
echo "Überprüfen des Status der Unit..."
sudo systemctl status $UNIT_NAME --no-pager

echo "Die Systemd-Unit $UNIT_NAME wurde erfolgreich eingerichtet und gestartet."
