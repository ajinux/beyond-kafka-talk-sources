## Slides 
Here are slides from my talk at Apache Kafka meetup on Dec 13, 2025 on topic `Beyond Kafka: Schema, Streams and Connectors`.

### Summary

This presentation explores the Apache Kafka ecosystem beyond basic producer-consumer patterns, covering three critical components:

**1. Schema Registry**
- Addresses challenges of raw JSON messaging (wasted storage, lack of contracts, no validation)
- Introduces serialization formats: Avro and Protobuf
- Demonstrates ~50% storage reduction with Avro compared to JSON
- Provides centralized schema management with version control and validation

**2. Kafka Connectors**
- Framework for integrating Kafka with external systems without custom code
- Source Connectors: Stream data from databases, APIs into Kafka
- Sink Connectors: Export Kafka data to Elasticsearch, S3, HDFS, and more
- Simplifies data pipeline architecture

**3. KSQL DB**
- Stream processing using SQL-like syntax
- Real-time data transformation, filtering, and aggregations
- Stream-stream and stream-table joins
- Windowing capabilities (tumbling, hopping, session windows)
- Materialized views for queryable state

The talk includes live demos and Python code examples for producers and consumers, with practical use cases for logs processing and error monitoring.