
FROM quay.io/jupyter/minimal-notebook:notebook-7.3.2

USER root

RUN apt-get update && apt-get install curl gcc -y

USER jovyan

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

RUN /home/jovyan/.cargo/bin/cargo install --locked evcxr_jupyter && /home/jovyan/.cargo/bin/evcxr_jupyter --install

RUN pip install ipywidgets ipycanvas matplotlib pandas sidecar plotly

COPY ./server_config.py /home/jovyan/.jupyter/jupyter_server_config.py

