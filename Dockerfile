FROM python:3.9-slim

ARG LANGUAGE_MODEL=en_core_web_md
ENV LANGUAGE_MODEL=${LANGUAGE_MODEL}

ARG SPACY_VERSION=3.5.1

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && \
  pip install spacy==${SPACY_VERSION} && \
  python -m spacy download ${LANGUAGE_MODEL}

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--log-level", "error"]
