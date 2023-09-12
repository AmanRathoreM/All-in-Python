# Date 21-05-2021

def encryption_tool_without_print(msg):
    msg2 = ''
    len_of_msg = len(msg)-1
    while len_of_msg >= 0:
        msg2 += msg[len_of_msg]
        len_of_msg -= 1
    return msg2


def encryption_tool_with_print(msg):
    msg2 = ''
    len_of_msg = len(msg)-1
    while len_of_msg >= 0:
        msg2 += msg[len_of_msg]
        print(msg2)
        len_of_msg -= 1
    return msg2


message_to_be_encrypted = input('Please enter the message.\n')
print(encryption_tool_without_print(message_to_be_encrypted))
print(5*'\n')
print(encryption_tool_with_print(message_to_be_encrypted))
