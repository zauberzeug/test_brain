FROM zauberzeug/rosys:0.10.2

RUN apt-get update && apt-get install -y libusb-1.0-0 libusb-1.0-0-dev && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install netifaces imgsize httpx itsdangerous aiofiles

