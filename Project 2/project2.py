from nltk.chat.util import Chat, reflections

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can i help you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot ?", ]
    ],
    [
        r"i need help with an order i have made",
        ["hello, can you specify what help do you need, if you need help with shipping please type 'shipping', if you need help wiht payment, please type 'payment', other wise, type'other'", ]
    ],
    [
        r"shipping",
        ["if the problem is with  late delivery? if type 'late delivery', if you did not receive item at all type 'not arrived'.", ]
    ],
    [
        r"payment",
        [" is the problem is 'extra fee'? type 'extra fee', if you are charged wrong price type 'wrong charge'.", ]
    ],
    [
        r"other",
        ["we will connect you with an agent as soon as possible.", ]
    ],
    [
        r"late delivery",
        ["Sorry for the late delivery we will check our provided GPS location for the order and notify you.", ]
    ],
    [
        r"no",
        ["Well that's okay. :(", ]
    ],
    [
        r"goodbye|bye| see ya",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]


def chatbot():
    print("Hi, I'm the chatbot you built"
          "\nWhat is your name? ")


chatbot()

chat = Chat(set_pairs, reflections)
print(chat)

chat.converse()
if __name__ == "__main__":
    chatbot()