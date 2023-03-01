number_of_messages_sent = int(input())
message = ""

for number in range(number_of_messages_sent):
    current_number = int(input())

    if current_number == 88:
        message = "Hello"
    elif current_number == 86:
        message = "How are you?"
    elif current_number < 88:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)
