import json

# Open JSON with morse dictionary
with open('./morse.json', 'r') as arquivo:
    data = json.load(arquivo)

'''
The input must contain spacing between each character. 
When there is spacing between words, three spaces must be used obligatorily.
'''
message = input("insert a morse message to be decoded: ")

if message == "":
    # message = "sou uma frase morse" | This will be shown if the input is null.
    message = "... --- ..-   ..- -- .-   ..-. .-. .- ... .   -- --- .-. ... ."

messageList = message.split("   ")
res = ""

for i in messageList:
    wordLetters = i.split(" ")
    for j in wordLetters:
        res += data["decode"][j]
    res += " "

print("your message: " + message + " means: " + res)