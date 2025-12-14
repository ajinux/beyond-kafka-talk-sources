import json
import random
from datetime import datetime
from confluent_kafka import Producer
"""
Produces review events to `product_reviews`.
Event structure:
{
    "review_id": review_id,
    "product_id": product_id,
    "user_id": user_id,
    "rating": rating,
    "review_text": review_text,
    "created_at": created_at
}
"""

def generate_random_review():
    """Generate a random product review message."""
    review_id = f"r-{random.randint(100000, 999999)}"
    product_id = f"p-{random.randint(1000, 9999)}"
    user_id = f"u-{random.randint(100, 999)}"
    rating = random.randint(1, 5)
    
    review_texts = [
        "Excellent product! Highly recommend.",
        "Good quality. Fast delivery.",
        "Not bad, but could be better.",
        "Terrible experience. Would not buy again.",
        "Amazing value for money!",
        "Product arrived damaged.",
        "Exactly as described. Very satisfied.",
        "Average quality, nothing special.",
        "Best purchase I've made this year!",
        "Disappointed with the quality.",
        "Great customer service and product.",
        "Took too long to arrive.",
        "Perfect! No complaints.",
        "Defective item received.",
        "Worth every penny!"
    ]
    
    review_text = random.choice(review_texts)
    created_at = int(datetime.utcnow().timestamp() * 1000)  # Epoch time in milliseconds
    
    return {
        "review_id": review_id,
        "product_id": product_id,
        "user_id": user_id,
        "rating": rating,
        "review_text": review_text,
        "created_at": created_at
    }


def delivery_callback(err, msg):
    """Callback for message delivery reports."""
    if err:
        print(f'✗ Message delivery failed: {err}')
    else:
        print(f'✓ Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')


def produce_messages(num_messages=10):
    """Produce random product review messages to Kafka."""
    # Configure Kafka producer
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'product-review-producer'
    }
    
    producer = Producer(conf)
    topic = 'product_reviews'
    
    print(f"Producing {num_messages} messages to topic '{topic}'...\n")
    
    for i in range(num_messages):
        review = generate_random_review()
        
        # Wrap in Kafka Connect schema format for sink connector
        kafka_connect_message = {
            "schema": {
                "type": "struct",
                "fields": [
                    {"field": "review_id", "type": "string"},
                    {"field": "product_id", "type": "string"},
                    {"field": "user_id", "type": "string"},
                    {"field": "rating", "type": "int32"},
                    {"field": "review_text", "type": "string"},
                    {"field": "created_at", "type": "int64", "name": "org.apache.kafka.connect.data.Timestamp"}
                ]
            },
            "payload": review
        }
        
        message_value = json.dumps(kafka_connect_message).encode('utf-8')
        
        # Produce message
        producer.produce(
            topic,
            value=message_value,
            callback=delivery_callback
        )
        
        print(f"Message {i+1}/{num_messages} queued: {json.dumps(review, indent=2)}")
        
        # Poll to handle delivery callbacks
        producer.poll(0)
    
    # Wait for all messages to be delivered
    print("\nWaiting for messages to be delivered...")
    producer.flush()
    
    print(f"\n✓ Successfully produced {num_messages} messages to '{topic}' topic")


if __name__ == "__main__":
    import sys
    
    # Get number of messages from command line argument or use default
    num_messages = 10
    if len(sys.argv) > 1:
        try:
            num_messages = int(sys.argv[1])
        except ValueError:
            print("Invalid number of messages. Using default (10).")
    
    produce_messages(num_messages)

