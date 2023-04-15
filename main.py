from chatterbot import ChatBot
import pickle
from chatterbot.trainers import ListTrainer
from chatterbot.storage import UserModel
import os
import re


def main():
    chatbot = ChatBot("Chatbot")
    #If you want the chatbot to only learn from the knowledge base and not everything the user inputs, replace the above line with this:
    #chatbot = ChatBot("Chatbot", read_only=True)

    #knowledgebase = pickle.load(open('knowledge_base.pickle', 'rb'))
    trainer = ListTrainer(chatbot)
    #trainer.train(knowledgebase)

    username = input("Please enter your name: ")
    user = UserModel(username)

    exit_conditions = (":q", "quit", "exit")
    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        elif re.search(r"^(I (understand|learned|know))", query):
            user.addSkill(query)
            print(f">> {chatbot.get_response(query)}")
        else:
            user.analyze(query)
            print(f">> {chatbot.get_response(query)}")

if __name__ == '__main__':
    main()