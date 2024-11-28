FROM python:3.12-bookworm

RUN apt update && apt install -y \
    sudo vim less ack-grep rsync wget curl cmake arp-scan iproute2 iw python3-pip python3-autopep8 libgeos-dev graphviz graphviz-dev v4l-utils psmisc sysstat \
    libgl1-mesa-glx ffmpeg libsm6 libxext6 \
    avahi-utils iputils-ping \
    jq \
    libusb-1.0-0 libusb-1.0-0-dev \
    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=zauberzeug
ARG USER_UID=1000
ARG USER_GID=1000

RUN addgroup --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && usermod -a -G dialout $USERNAME \
    && usermod -a -G tty $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

RUN python3 -m pip install --upgrade pip

WORKDIR /app
COPY requirements.txt ./

RUN python3 -m pip install --user -r requirements.txt

WORKDIR /root/.lizard
RUN CURL="curl -s https://api.github.com/repos/zauberzeug/lizard/releases" && \
    ZIP=$(eval "$CURL/latest" | jq -r '.assets[0].id') && \
    eval "$CURL/assets/$ZIP -LJOH 'Accept: application/octet-stream'" && \
    unzip *zip && \
    rm *zip && \
    ls -lha

# for Lizard monitor
RUN python3 -m pip install --no-cache prompt-toolkit

WORKDIR /app
COPY --chown=${USERNAME}:${USER_GID} test_brain ./test_brain/

CMD python3 main.py
