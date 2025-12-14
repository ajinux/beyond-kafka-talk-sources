import json
import random
import argparse
from datetime import datetime, timedelta
import time
from confluent_kafka import Producer
"""
Topic: logs
Event structure:
{
    "timestamp": timestamp,
    "app": app,
    "level": level,
    "msg": msg
}
"""

# Sample data for random log generation
APPS = ["order-service", "payment-service", "user-service", "inventory-service", "notification-service"]
LEVELS = ["INFO", "WARN", "ERROR", "DEBUG"]
MESSAGES = {
    "INFO": [
        "request processed successfully",
        "user logged in",
        "cache updated",
        "database connection established",
        "job completed"
    ],
    "WARN": [
        "high memory usage detected",
        "slow query detected",
        "retry attempt failed",
        "deprecated API called",
        "connection pool exhausted"
    ],
    "ERROR": [
        "disk full",
        "database connection failed",
        "out of memory",
        "null pointer exception",
        "service unavailable",
        "authentication failed"
    ],
    "DEBUG": [
        "entering method",
        "variable value checked",
        "cache hit",
        "loop iteration completed",
        "condition evaluated"
    ]
}


def generate_random_log():
    """Generate a random log message"""
    level = random.choice(LEVELS)
    app = random.choice(APPS)
    msg = random.choice(MESSAGES[level])
    
    # Generate a timestamp within the last 24 hours
    now = datetime.now()
    random_seconds = random.randint(0, 86400)  # 24 hours in seconds
    timestamp = (now - timedelta(seconds=random_seconds)).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    return {
        "timestamp": timestamp,
        "app": app,
        "level": level,
        "msg": msg
    }


def delivery_report(err, msg):
    """Callback for message delivery reports"""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')


def produce_logs(num_messages, topic="logs", bootstrap_servers="localhost:9092"):
    """Produce random log messages to Kafka"""
    
    # Configure the producer
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'log-producer'
    }
    
    producer = Producer(conf)
    
    print(f"Producing {num_messages} log messages to topic '{topic}'...")
    
    for i in range(num_messages):
        log_message = generate_random_log()
        
        # Serialize to JSON
        message_json = json.dumps(log_message)
        
        # Produce message
        producer.produce(
            topic,
            key=log_message["app"],  # Use app name as key for partitioning
            value=message_json,
            callback=delivery_report
        )
        
        # Trigger delivery report callbacks
        producer.poll(0)
        
        if (i + 1) % 10 == 0:
            print(f"Produced {i + 1}/{num_messages} messages")
        time.sleep(1)
    
    # Wait for all messages to be delivered
    print("Waiting for all messages to be delivered...")
    producer.flush()
    
    print(f"Successfully produced {num_messages} log messages!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce random log messages to Kafka")
    parser.add_argument("num_messages", type=int, help="Number of messages to produce")
    parser.add_argument("--topic", type=str, default="logs", help="Kafka topic name (default: logs)")
    parser.add_argument("--bootstrap-servers", type=str, default="localhost:9092", 
                        help="Kafka bootstrap servers (default: localhost:9092)")
    
    args = parser.parse_args()
    
    if args.num_messages <= 0:
        print("Error: Number of messages must be greater than 0")
        exit(1)
    
    produce_logs(args.num_messages, args.topic, args.bootstrap_servers)
