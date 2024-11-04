FROM zauberzeug/rosys:0.18.6

RUN apt-get update && apt-get install -y libusb-1.0-0 libusb-1.0-0-dev && rm -rf /var/lib/apt/lists/*