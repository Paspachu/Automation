def decode(message_file):
    # Read the meassage file
    with open(message_file, "r") as f:
        lines = f.readlines()
  
    # Initialize an empty dictionary
    messages = {}

    # Save all the messages in the file
    for line in lines:
        # Split the line by space and get the first element as the number
        number = int(line.split()[0])
        # Get the second element as the word
        word = line.split()[1]
        # Save the word to messages
        messages[number] = word

    # Sort all the messages in increasing order
    messages_sorted = dict(sorted(messages.items()))

    # Initialize the index variable and a string variable to store the decoded message
    i = 1
    decoded_message = ""

    # Loop until the index of end of the pyramid is out of bound
    while i*(i+1)/2 <= len(messages_sorted):
        # Add the word at the end of the pyramid index
        decoded_message += messages_sorted[i*(i+1)/2] + " "
        i += 1

    return decoded_message[:-1]

print(decode("messagefile.txt"))