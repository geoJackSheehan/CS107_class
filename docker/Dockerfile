FROM docker.io/ubuntu:latest

# update aptitude
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=US/Eastern
RUN apt-get update && apt-get -y --fix-missing upgrade

# install aptitude essentials
RUN apt-get -y install \
    build-essential \
    clang \
    man \
    manpages-posix \
    pkg-config \
    bash-completion \
    openssh-client \
    git \
    vim \
    emacs \
    nano \
    ne \
    tilde \
    vifm \
    rsync \
    wget \
    curl \
    tmux \
    tmate \
    texlive-latex-base \
    texlive-latex-extra \
    pandoc

RUN apt-get -y install \
    python3-dev \
    python3-pip \
    python3-pybind11 \
    python3-numpy \
    python3-matplotlib \
    python3-pandas \
    python3-scipy \
    python3-xlrd

RUN python3 -m pip install meson ninja
RUN python3 -m pip install cmake
RUN python3 -m pip install gcovr

RUN update-alternatives --set editor /usr/bin/vim.basic

# Enable documentation
RUN yes | unminimize

CMD ["/bin/bash"]
