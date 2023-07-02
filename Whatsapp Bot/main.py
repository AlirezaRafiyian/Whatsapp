import pywhatkit
import time


""" 
It's better to take the input from user if the number of messages is not known

"""
# Array of messages to send
messagesToSend = [
    {
        'recipient': 'Number or Channel Name',
        'message': 'Hello, how are you?'
    },
    {
        'recipient': 'Number or Channel Name',
        'message': 'Just checking in. Hope you are doing well.'
    },
    {
        'recipient': 'Number or Channel Name',
        'message': 'This is a message to the channel.'
    }
    # Add more messages as needed
]

# Send multiple messages
for message in messagesToSend:
    recipient = message['recipient']
    text = message['message']

    # Send message via WhatsApp
    # Always set close tab True especially when there are more than 10 message.
    pywhatkit.sendwhatmsg_instantly(recipient, text, tab_close=True, close_time=3)

    # Wait for message to be sent
    time.sleep(6)

# End the script
print("Messages sent successfully!")
