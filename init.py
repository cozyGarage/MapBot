import sys

# Check Python version
if sys.version_info < (3, 10):
    print("Error: MapBot requires Python 3.10 or higher.")
    print(f"You are using Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print("Please upgrade your Python version.")
    sys.exit(1)

from chatbot import setup
from chatbot import message_to_bot

print("MapBot 2025 Edition - Starting up...")
print("Loading NLP models and training data...")
clf, learn_response = setup()
print("Ready! Type 'bye' to exit.\n")

while(True):
	received_message = input("You: ")
	send_message, learn_response = message_to_bot(received_message,clf,learn_response)
	print("MapBot: "+send_message)