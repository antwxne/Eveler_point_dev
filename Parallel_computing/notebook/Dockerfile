FROM python:3.11.7

WORKDIR /build

# install mojo
RUN curl -ssL https://magic.modular.com/5efccf54-e3ae-4105-8dfa-48cada3ae79a | bash
ENV PATH="/root/.modular/bin/:$PATH"

WORKDIR /app
COPY ./mojoproject.toml ./mojoproject.toml
RUN magic install
EXPOSE 8888
CMD magic run jupyter lab --allow-root --no-browser --ip=0.0.0.0 --port=8888 --NotebookApp.token='' --NotebookApp.password=''
