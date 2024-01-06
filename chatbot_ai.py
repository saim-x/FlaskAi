# import google.generativeai as palm

# API_KEY = "AIzaSyDouqB56L-MU831RWff2SKSydGjad2wrfA"
# palm.configure(api_key=API_KEY)

# examples = [
#     ('Hello, how can i be your assistant?', 'I need help with my university studies.'),
# ]

# prompt = "I need help in my universities studies, Can you help me pls"
# response = palm.chat(
#     messages=prompt,
#     temperature=0.2,
#     context='Speak like a professor',
#     examples=examples,
# )

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Exiting the chat.")
#         break

#     response = response.reply(user_input)
#     print(f"Bot: {response.last}")




# chatbot_ai.py
import google.generativeai as palm

class Chatbot:
    def __init__(self):
        API_KEY = "AIzaSyDouqB56L-MU831RWff2SKSydGjad2wrfA"
        palm.configure(api_key=API_KEY)

        examples = [
            ('Hello, how can i be your assistant?', 'I need help with my university studies.'),
        ]

        self.response = palm.chat(
            messages="I need help in my universities studies, Can you help me pls",
            temperature=0.7,
            context='Speak like a professor',
            examples=examples,
        )

    def generate_response(self, user_input):
        # Handle user input and generate a response using the chatbot logic
        self.response = self.response.reply(user_input)
        return self.response.last
