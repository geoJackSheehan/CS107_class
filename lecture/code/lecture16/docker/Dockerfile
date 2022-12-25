# base image
FROM docker.io/fedora:latest

RUN dnf -y update

# install basic Python development and frequently used packages
RUN dnf -y install \
    python-devel \
    python-build \
    python-numpy \
    python-pandas \
    python-matplotlib \
    python-pytest \
    python-pytest-cov

# we could add other custom Python code if we needed to.  For example the
# cs107_package from lecture 9 (we will not do it because we will build this
# package using this container!)
#
# RUN python3 -m pip install -i https://test.pypi.org/simple/ Fall2022-CS107

# you can COPY a local file into the container image (the file will be
# added to the image file system)
COPY local_file .

# you can use any shell commands with the RUN command
RUN echo "Hello CS107/AC207 Docker!" >hello.txt

# entry point is bash shell
CMD ["/bin/bash"]

# add non-root user (optional, for GitHub Actions user must be root)
# RUN useradd -m cs107
# WORKDIR /home/cs107
# USER cs107
