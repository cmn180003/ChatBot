from chatterbot import ChatBot
import pickle
from chatterbot.trainers import ListTrainer

def main():
    chatbot = ChatBot("Chatbot")
    #If you want the chatbot to only learn from the knowledge base and not everything the user inputs, replace the above line with this:
    #chatbot = ChatBot("Chatbot", read_only=True)

    #knowledgebase = pickle.load(open('knowledge_base.pickle', 'rb'))
    trainer = ListTrainer(chatbot)
    #trainer.train(knowledgebase)

    exit_conditions = (":q", "quit", "exit")
    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        else:
            print(f">> {chatbot.get_response(query)}")

if __name__ == '__main__':
    main()