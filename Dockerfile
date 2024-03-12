FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

COPY ./src ./src

ENTRYPOINT ["streamlit", "run"]

CMD ["./src/main.py"]