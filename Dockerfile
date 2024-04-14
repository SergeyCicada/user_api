FROM ubuntu:latest
LABEL authors="skelme"

ENTRYPOINT ["top", "-b"]