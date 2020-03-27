FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
ENV LANG C.UTF-8

USER root
RUN apt-get -qqy update
RUN apt-get -qqy --no-install-recommends install \
  wget \
  firefox \
  x11vnc \
  xvfb \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  python3-pip \
  curl \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz \
  && tar -xzf /tmp/geckodriver.tar.gz -C /usr/bin && rm -rf /tmp/geckodriver.tar.gz

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "-m", "src.find_diapers" ]