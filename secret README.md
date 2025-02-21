# Simple Secret Code Generator in Python

## Description
This is a simple Secret Code Generator written in Python. The program allows you to encode and decode messages based on a custom set of rules.

## Encoding Rules:
The program moves the first character of the string to the end.
Then, it adds 3 characters at the start and the end of the string.
# Output for Encoding:
           https://github.com/Coderh142/Python-projects-/blob/34aeb028b50ed7d1caa952787396016c1531243c/Encoding.png
## Example:
            hello world  ---> NjWello worldhNjW

## Decoding Rules:
To decode the message, simply apply the reverse of the encoding rules. The encoded message is decoded by:

Removing the last 3 characters and the first 3 characters.
Then, the last character of the string is moved back to it's original position.
# Output for Decoding:
                  
## Example:
            NjWello worldhNjW  ---> hello world
      
## Special Cases:
  If the string contains 3 or more words, the encoding and decoding rules are applied as mentioned above.
  If the string contains 2 characters, characters are just swapped (no additional characters are added).
  
  ## How to Use:
  Run the Python program.
  When prompted, enter 1 to encode or enter 0 to decode a message.
  Input your message when prompted.
  The program will apply the rules and show the resulting encoded or decoded message.
  
## Example Usage:
## *Copy
Enter action (1 for encode, 0 for decode): 1
Enter your message: hello world
Encoded message: NjWello worldhNjW

Enter action (1 for encode, 0 for decode): 0
Enter your message: NjWello worldhNjW
Decoded message: hello world

## Requirements:
Python 3.x
Setup Instructions
Install Python on your system (if not already installed).
Download or clone the repository.
Run the Python script to start the program.

## License:
This project is free to use and modify.
