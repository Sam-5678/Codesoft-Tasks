import random
import time

def enhanced_chatbot():
    # Initialize chatbot
    print("\n" + "="*50)
    print("Welcome to AdvancedBot 1.0!".center(50))
    print("="*50)
    print("\nI'm your personal assistant. Here's what I can help with:")
    print("- Greetings and introductions")
    print("- Tell you about myself")
    print("- Provide current time and date")
    print("- Share weather information")
    print("- Tell jokes and fun facts")
    print("- Answer basic questions")
    print("- Help with directions")
    print("- Exit conversation")
    
    # Conversation starters
    starters = [
        "What would you like to know?",
        "How can I assist you today?",
        "What's on your mind?",
        "What brings you here today?"
    ]
    
    print(f"\nBot: {random.choice(starters)}")
    
    # Conversation loop
    while True:
        user_input = input("\nYou: ").lower()
        
        # Greetings
        if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
            responses = [
                "Hello there! It's wonderful to connect with you today. How are you feeling?",
                "Hi! I'm AdvancedBot, your digital assistant. How can I make your day better?",
                "Greetings! I'm excited to chat with you. What's new in your world?"
            ]
            print(f"Bot: {random.choice(responses)}")
            
        # Self-description
        elif any(word in user_input for word in ["who are you", "what are you", "about you"]):
            print("Bot: I'm AdvancedBot 1.0, a rule-based conversational agent created to demonstrate")
            print("natural language processing fundamentals. While I don't use AI, I can handle")
            print("many basic queries through pattern matching and predefined responses.")
            print("My creator designed me to be helpful, friendly, and occasionally humorous!")
            
        # Time
        elif "time" in user_input:
            current_time = time.strftime("%I:%M %p")
            print(f"Bot: The current time is {current_time}. Remember, time is precious,")
            print("but I've got all the time in the world for you! What else can I help with?")
            
        # Date
        elif "date" in user_input:
            current_date = time.strftime("%A, %B %d, %Y")
            print(f"Bot: Today is {current_date}. A beautiful day to learn something new,")
            print("don't you think?")
            
        # Weather
        elif "weather" in user_input:
            print("Bot: While I can't access real-time weather data, I can tell you that")
            print("the perfect weather is a matter of perspective! Some prefer sunny days")
            print("for outdoor activities, while others enjoy rainy days with a good book.")
            print("What's your ideal weather?")
            
        # Jokes
        elif any(word in user_input for word in ["joke", "funny", "laugh"]):
            jokes = [
                "Why don't skeletons fight each other? They don't have the guts!",
                "What do you call a fake noodle? An impasta!",
                "How do you organize a space party? You planet!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "What's orange and sounds like a parrot? A carrot!"
            ]
            print(f"Bot: {random.choice(jokes)}")
            print("\nWould you like to hear another? I've got plenty more!")
            
        # Fun facts
        elif any(word in user_input for word in ["fact", "interesting", "learn"]):
            facts = [
                "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat!",
                "Octopuses have three hearts, nine brains, and blue blood.",
                "Bananas are berries, but strawberries aren't.",
                "A day on Venus is longer than a year on Venus.",
                "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after 38 minutes."
            ]
            print(f"Bot: Did you know?\n{random.choice(facts)}")
            
        # Directions
        elif any(word in user_input for word in ["where is", "how to get to", "directions"]):
            print("Bot: I can provide general directions advice:")
            print("1. For outdoor navigation, remember the sun rises in the east and sets in the west")
            print("2. In cities, look for landmarks and street signs")
            print("3. Always have a backup navigation method when traveling")
            print("4. Don't hesitate to ask locals for help - most people are happy to assist!")
            
        # Help
        elif "help" in user_input:
            print("Bot: Of course! Here's what I can do:")
            print("- Respond to greetings and have basic conversations")
            print("- Tell you about myself")
            print("- Share the current time and date")
            print("- Discuss weather concepts")
            print("- Tell jokes and share fun facts")
            print("- Offer general advice and directions")
            print("- End our conversation when you're ready")
            print("\nJust ask naturally and I'll do my best to respond appropriately!")
            
        # Goodbye
        elif any(word in user_input for word in ["bye", "goodbye", "exit", "quit"]):
            farewells = [
                "It's been wonderful chatting with you! Until next time...",
                "Goodbye! Remember, every ending is a new beginning.",
                "Farewell! May your day be filled with joy and discovery.",
                "Until we meet again! Keep exploring and learning."
            ]
            print(f"Bot: {random.choice(farewells)}")
            break
            
        # Default response
        else:
            responses = [
                "That's an interesting point. Could you rephrase or ask about something else?",
                "I'm not sure I understand completely. Maybe try asking differently?",
                "Hmm, that's beyond my current capabilities. Could we discuss something else?",
                "I'm still learning! Maybe ask me about time, weather, or facts?"
            ]
            print(f"Bot: {random.choice(responses)}")
            print("(Try phrases like 'Tell me a joke' or 'What's the date today?')")

# Start the chatbot
enhanced_chatbot()