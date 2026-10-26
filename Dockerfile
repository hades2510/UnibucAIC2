FROM spark:4.1.3-scala2.13-java17-python3-ubuntu

ENV PYSPARK_PYTHON=python3 \
    PYSPARK_DRIVER_PYTHON=python3 \
    PYTHONUNBUFFERED=1 \
    HOME=/tmp \
    SPARK_LOCAL_IP=127.0.0.1 \
    SPARK_DRIVER_BIND_ADDRESS=127.0.0.1

WORKDIR /workspace

# Mount host scripts at /workspace and pass a script path when running.
# Keep Spark's entrypoint for user setup and process cleanup.
ENTRYPOINT ["/opt/entrypoint.sh", "driver", "--master", "local[2]"]
CMD ["--help"]
