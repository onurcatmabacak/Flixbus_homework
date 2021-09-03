 The client send a message in json format via tcp protocol, the server accepts this message and stores it in a txt file if certain conditions are met.
 
The conditions are: If there is a 10 second gap between messages from the client, store it. If the number of messages is 10 or bigger store it in the txt file.

Improvements: A log file needs to be implemented so that every 10 second the message will be appended into the log file.
 
