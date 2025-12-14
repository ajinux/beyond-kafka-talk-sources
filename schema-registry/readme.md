## Run schema-registry
```
docker run --rm \
  --name schema-registry \
  -p 8082:8081 \
  -e SCHEMA_REGISTRY_HOST_NAME=schema-registry \
  -e SCHEMA_REGISTRY_LISTENERS=http://0.0.0.0:8081 \
  -e SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS=PLAINTEXT://host.docker.internal:9092 \
  confluentinc/cp-schema-registry:7.6.1
```
## Produce messages with and without schema for comparison
1. `uv run schema_registry/produce_noschema.py` 
2. `uv run schema_registry/produce.py`
## Inspect kafka topic in disk to see the difference
> bin/kafka-dump-log.sh --print-data-log --files /tmp/kafka-logs/orders-0/

## Check out the slides for workings and architecture