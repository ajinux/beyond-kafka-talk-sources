# Connector

## Objective
- Read events from the `product_reviews` Kafka topic and insert them into a PostgreSQL table

## Setup Kafka Connector
1. Add `kafka-connect-jdbc-10.8.4.jar` and `postgresql-42.4.4.jar` JARs inside the `jdbc` directory of the specified `plugin.path` in `connect-standalone.properties`
2. Run the connector (either via Docker or locally):
```bash
bin/connect-standalone.sh config/connect-standalone.properties
```

## Setup PostgreSQL
1. Start the PostgreSQL server (either via Docker or locally)
2. Create the table in the public schema:
```sql
CREATE TABLE IF NOT EXISTS product_reviews ( 
    review_id text PRIMARY KEY,
    product_id text,
    user_id text,
    rating int,
    review_text text,
    created_at timestamptz 
);
```

## Start Sinking
1. Start producing `product_reviews` events by running:
```bash
uv run connector/produce.py 30
```
2. Register the `product-reviews-pg-sink` connector by calling this endpoint:
```bash
curl --location 'http://localhost:8083/connectors' \
--header 'Content-Type: application/json' \
--data '{
    "name": "product-reviews-pg-sink",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "tasks.max": "1",
        "topics": "product_reviews",
        "connection.url": "jdbc:postgresql://localhost:5432/ajith",
        "connection.user": "postgres",
        "connection.password": "ajith",
        "insert.mode": "insert",
        "pk.mode": "none",
        "auto.create": "false",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "true",
        "delete.enabled": "false"
    }
}'
```

Now all events (both produced and being produced) will automatically be inserted into the PostgreSQL table without writing a single line of code!