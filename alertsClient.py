import paho.mqtt.client as mqtt
import sys

# Callback function when the client connects to the MQTT server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker")
        # Subscribe to the topic planes/watchforLong/# for all locations
        client.subscribe("planes/watchforLong/#")
    else:
        print(f"Failed to connect, return code {rc}")

# Callback function when a message is received from the subscribed topic
def on_message(client, userdata, message):
    try:
        # Extract the topic (e.g., planes/watchforLong/mesa) and the payload (message)
        topic = message.topic
        payload = message.payload.decode()

        # Extract the location from the topic (the last part of the topic)
        location = topic.split('/')[-1]

        # Print the message in the format "location - message received"
        print(f"{location} - {payload}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Main function to handle the connection to the MQTT server
def connect_mqtt(mqtt_server, mqtt_port, mqtt_id=None, mqtt_pass=None):
    # Create an MQTT client instance
    client = mqtt.Client()

    # Set the username and password if provided
    if mqtt_id and mqtt_pass:
        client.username_pw_set(mqtt_id, mqtt_pass)

    # Assign the callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT server
    client.connect(mqtt_server, mqtt_port, 60)

    # Start the MQTT client loop
    client.loop_forever()

# Entry point of the program
if __name__ == "__main__":
    # Check if the user provided enough command line arguments
    if len(sys.argv) < 3:
        print("Usage: python mqtt_client.py <MQTT_SERVER> <MQTT_PORT> [MQTT_ID] [MQTT_PASS]")
        sys.exit(1)

    # Get the MQTT server and port from the command line arguments
    mqtt_server = sys.argv[1]
    mqtt_port = int(sys.argv[2])

    # Get the optional MQTT ID and Password
    mqtt_id = sys.argv[3] if len(sys.argv) > 3 else None
    mqtt_pass = sys.argv[4] if len(sys.argv) > 4 else None

    # Connect to the MQTT server and subscribe to the topic
    connect_mqtt(mqtt_server, mqtt_port, mqtt_id, mqtt_pass)
