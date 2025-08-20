print("Bot:Hi!Type 'q' to exit")
responses={"hello":"hi, how can i help you?",
           "ai":"artificial intelligence",
           "ml":"machine learning",
           "python":"python is a programming language",
           "q":"bye, have a nice day!"}
while True:
    query=input("You:")
    if query=="q":
        print("Bot:",responses["q"])
        break
    elif query in responses:
        print("Bot:",responses[query])