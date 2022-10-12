FROM gitpod/workspace-base

# Install ghcup and add it to path
RUN sudo curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
ENV PATH="/home/gitpod/.ghcup/bin:${PATH}"

# Install hls and stack
RUN ghcup install hls
RUN ghcup install stack

# Install zlib
RUN sudo apt install -y zlib1g
