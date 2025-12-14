## Docker command
```
docker run --rm \
  --name ksqldb-server \
  -p 8088:8088 \
  -e KSQL_LISTENERS="http://0.0.0.0:8088" \
  -e KSQL_BOOTSTRAP_SERVERS="host.docker.internal:9092" \
  -e KSQL_KSQL_LOGGING_PROCESSING_STREAM_AUTO_CREATE="true" \
  -e KSQL_KSQL_LOGGING_PROCESSING_TOPIC_AUTO_CREATE="true" \
  confluentinc/ksqldb-server:latest
```

## Docker exec
```
docker run -it \
   confluentinc/ksqldb-cli:latest \
   ksql http://host.docker.internal:8088
```

## Commands
### Create logs_stream
```
CREATE STREAM logs_stream (
  timestamp VARCHAR,
  app VARCHAR,
  level VARCHAR,
  msg VARCHAR
) WITH (
  KAFKA_TOPIC='logs',
  VALUE_FORMAT='JSON'
);
```
## Create order service error streams
```
CREATE STREAM order_errors AS
SELECT timestamp, app, msg
FROM logs_stream
WHERE level = 'ERROR'
  AND app = 'order-service';
```

## Create a table
```
CREATE TABLE app_error_count AS
SELECT app, COUNT(*) 
FROM logs_stream
WHERE level='ERROR'
GROUP BY app;
```