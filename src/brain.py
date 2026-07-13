import ollama
from src.memory import load_memory, save_memory

conversation_history = load_memory()

faq = {
    "student portal": "You can access your exam results on i-Ma'luum.",
    "Dr. Hasan": "Dr. Hasan is a handsome and cool lecturer."
    # ... add the rest of your FAQ entries here
}

def get_response(text):
    for key in faq:
        if key in text.lower():
            return faq[key]

    conversation_history.append({'role': 'user', 'content': text + " Answer in 1 short sentence."})
    active_memory = conversation_history[-20:]

    try:
        response = ollama.chat(model='llama3.2', messages=active_memory)
        reply = response['message']['content']
        conversation_history.append({'role': 'assistant', 'content': reply})
        save_memory(conversation_history)
        return reply
    except:
        return "I cannot connect to Ollama."