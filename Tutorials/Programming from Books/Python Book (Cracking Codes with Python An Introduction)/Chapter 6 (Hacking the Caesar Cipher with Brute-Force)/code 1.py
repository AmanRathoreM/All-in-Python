# Date 23-05-2021

message = input('Please Enter the message!\n')
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
msg = []
# Loop through every possible key:
for key in range(len(symbols)):
    translated_message = ''

    for symbol in message:
        if symbol in symbols:
            symbolIndex = symbols.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(symbols)

            translated_message = translated_message + symbols[translatedIndex]

        else:
            translated_message = translated_message + symbol

    msg.append(translated_message)
n = 0
for i in msg:
    print('Key', n, '----', i)
    n += 1
