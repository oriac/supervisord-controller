FROM ubuntu

RUN apt-get update && apt-get install -y \
    python \
    python-setuptools \
    python-pip

# Install Supervisor.
RUN \
  apt-get install -y supervisor && \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

RUN pip install pika

RUN mkdir /consumers

WORKDIR /consumers

ADD . /consumers/

RUN ln -s /consumers/consumer.conf /etc/supervisor/conf.d

# Define working directory.
WORKDIR /etc/supervisor/conf.d

# Define default command.
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
