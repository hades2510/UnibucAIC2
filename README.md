# Run PySpark scripts

Keep your scripts, `Dockerfile`, and `docker-compose.yml` in the same folder.
Open a terminal in that folder with Docker running.

## 1. Build

```bash
docker compose build
```

## 2. Start

```bash
docker compose up
```

Leave this terminal open. Press **Ctrl+C** here when you want to stop the container.

## 3. Run scripts

Open a second terminal in the same folder and run:

```bash
docker compose exec pyspark_dev /opt/spark/bin/spark-submit --master "local[*]" snippet_1.py
docker compose exec pyspark_dev /opt/spark/bin/spark-submit --master "local[*]" snippet_2.py
docker compose exec pyspark_dev /opt/spark/bin/spark-submit --master "local[*]" snippet_3.py
```

You can edit your scripts and run them again without rebuilding or restarting.

