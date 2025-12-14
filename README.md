# Beyond Kafka: Schema, Streams & Connectors

🎤 **Slides are live at:** [https://ajinux.github.io/beyond-kafka-talk-sources/slides/reveal.js/](https://ajinux.github.io/beyond-kafka-talk-sources/slides/reveal.js/)  
*(Refresh the slide if you see any mermaid error)*

This repository contains code examples and presentation materials for exploring advanced Kafka features including Schema Registry, Kafka Connectors, and KSQL DB.

## Overview

Apache Kafka is a distributed event streaming platform that enables high-throughput, scalable, and fault-tolerant messaging. This talk goes beyond basic Kafka usage to explore three powerful ecosystem components that enhance Kafka's capabilities:

- **Schema Registry** - Centralized schema management and validation
- **Kafka Connectors** - Integration framework for external systems
- **KSQL DB** - Stream processing with SQL-like queries

## 📝 [Schema Registry](./schema-registry/readme.md)

Learn how Schema Registry provides data contract enforcement, message validation, and storage optimization through serialization formats like Avro and Protobuf.

**Key Benefits:**
- Reduce storage by ~50% compared to raw JSON
- Enforce data contracts between producers and consumers
- Support schema evolution
- Validate messages at production time

**Try it:** [See schema-registry/readme.md](./schema-registry/readme.md)
- Run Schema Registry with Docker
- Compare message sizes between JSON and Avro formats
- Inspect Kafka topic data on disk to see the difference

## 🔌 [Kafka Connectors](./connector/readme.md)

Discover how Kafka Connect provides a framework for integrating Kafka with external systems without writing custom code.

**Connector Types:**
- **Source Connectors** - Import data from external systems into Kafka
- **Sink Connectors** - Export data from Kafka to external systems

**Demo Example:** [See connector/readme.md](./connector/readme.md)
- Read events from `product_reviews` Kafka topic
- Automatically sink data to PostgreSQL using JDBC connector
- No custom consumer code required

## 💾 [KSQL DB](./ksqldb/readme.md)

Explore stream processing capabilities using SQL-like queries for real-time data transformation, filtering, and aggregations.

**Features:**
- Real-time data filtering and transformation
- Aggregations with GROUP BY (COUNT, SUM, AVG)
- Stream-stream and stream-table joins
- Windowing support (tumbling, hopping, session)
- Materialized views

**Demo Example:** [See ksqldb/readme.md](./ksqldb/readme.md)
- Create streams from Kafka topics
- Filter application error logs
- Aggregate error counts by application

## 🎬 Presentation

View the interactive slides in `slides/reveal.js/index.html` for:
- Kafka architecture diagrams
- Schema Registry workflow
- Connector patterns
- KSQL DB examples
- Live demos

## Getting Started

### Prerequisites
- Docker
- Python 3.x with `uv` package manager
- Kafka cluster running locally on port 9092

### Running the Examples

1. **Schema Registry Demo**: See [schema-registry/readme.md](./schema-registry/readme.md)
2. **Kafka Connector Demo**: See [connector/readme.md](./connector/readme.md)
3. **KSQL DB Demo**: See [ksqldb/readme.md](./ksqldb/readme.md)

## Author

**Ajithkumar Sekar**  
Senior Software Developer at Weave Communications
