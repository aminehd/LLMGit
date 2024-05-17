From mcr.microsoft.com/devcontainers/python:3.9
COPY .devcontainers/post_create.sh /tmp
COPY .devcontainers/interpreter_warning.py /tmp

RUN chmod +x /tmp/post_create.sh && /tmp/post_create.sh
# ALSO install the the poetry stuff and move it to right place or add a symlinc in task part

