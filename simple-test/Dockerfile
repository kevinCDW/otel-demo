FROM opensuse/tumbleweed:latest

RUN zypper refresh && \
    zypper install -y python311 python311-pipx python311-pip

RUN pipx install poetry && pipx ensurepath
ENV PATH=/root/.local/bin:$PATH
COPY pyproject.toml /app/pyproject.toml
COPY server.py /app/server.py

WORKDIR /app
RUN poetry install 
ENV OTEL_TRACES_EXPORTER=otlp
ENV OTEL_METRICS_EXPORTER=otlp
ENV OTEL_LOGS_EXPORTER=otlp
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://collector:4318
ENV OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
CMD ["poetry", "run", "opentelemetry-instrument", "flask", "--app", "server", "run", "--host", "0.0.0.0"]
