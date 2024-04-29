FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt update && apt install -y dbus-x11 gnome-keyring

# enable keyring
COPY .bashrc.keyring /home/vscode/.bashrc.keyring
RUN echo ". ~/.bashrc.keyring" >> /home/vscode/.bashrc
