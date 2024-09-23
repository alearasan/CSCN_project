# Use a base image with Asterisk pre-installed
FROM andrius/asterisk:alpine-20.5.2

RUN apk update \
            apk add --update tcptraceroute \
            && apk add --update tcpdump \
            && apk add --update bind-tools \
            && apk add --update bash

# Copy Asterisk configuration files
COPY asterisk_config/* /etc/asterisk/
COPY sounds/* /var/lib/asterisk/sounds/

# Expose SIP and RTP ports
EXPOSE 5060/udp
EXPOSE 5038
#EXPOSE 10000-10100/udp
# Start Asterisk
CMD ["asterisk", "-f"]