# Date 22-05-2021
from pyperclip import copy as co


def caesar_cipher(msg='This is my secret message.', key=13, mode='encrypt', symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.', copy_or_not='yes'):
    '''
    Use:
        This function can be used to deal with Caesar Cipher

    Parameters:
        caesar_cipher(msg='This is my secret message.', key=13, mode='encrypt', symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.', copy_or_not='yes'):

    Example 1:
        print(caesar_cipher('This is an example of Caesar Cipher.', 2))
    Output of Example 1:
        Vjku?ku?cp?gzcorng?qh?Ecguct?EkrjgtB!

    Example 2:
        print(caesar_cipher('Vjku?ku?cp?gzcorng?qh?Ecguct?EkrjgtB', 2, 'decrypt'))
    Output of Example 2:
        This is an example of Caesar Cipher.

    Example 3:
        print(caesar_cipher('This is an example of Caesar Cipher.', 2, 'encrypt','qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM.'))
    Output of Example 3:
        UkpfWpfWd WtvdQsxtWahWBdtfdyWBpsktyw

    Example 4:
        print(caesar_cipher('UkpfWpfWd WtvdQsxtWahWBdtfdyWBpsktyw', 2, 'decrypt','qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM.'))
    Output of Example 4:
        This is an example of Caesar Cipher.

    Returns:
        It returns translated msg

    Note:
        The translated message is also be copied in your clipboard to disable it use this syntax.
        Syntax:
            print(caesar_cipher('This is an example of Caesar Cipher.', 2, 'encrypt','qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM.','No'))
    '''
    copy_or_not = copy_or_not.lower()
    mode = mode.lower()
    key = int(key)
    translated_message = ''
    for Symbol in msg:
        if Symbol in symbols:
            symbol_index = int(symbols.find(Symbol))
            if mode == 'encrypt':
                translated_index = symbol_index + key
            elif mode == 'decrypt':
                translated_index = symbol_index - key
            if translated_index >= len(symbols):
                translated_index -= len(symbols)
            elif translated_index < 0:
                translated_index += len(symbols)
            translated_message += str(symbols[translated_index])
        else:
            translated_message += str(Symbol)
    if copy_or_not == 'yes':
        co(translated_message)
    return translated_message


# if __name__ == '__main__':
#     print(caesar_cipher.__doc__)
#     print(caesar_cipher('Kv?uqwpfu?rncwukdng?gpqwijB', 2, 'decrypt'))
#     print(caesar_cipher('XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V', 22, 'decrypt'))
