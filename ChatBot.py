import tkinter as tk
from tkinter import scrolledtext
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question

here's the conversation history : {context}

Question : {question}
Answer:

"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    def on_enter_pressed(event=None):
        user_input = entry.get()
        if user_input.lower() == "exit":
            root.quit()
        else:
            result = chain.invoke({"context": context_var.get(), "question": user_input})
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, f"You: {user_input}\n")
            chat_area.insert(tk.END, f"bot: {result}\n")
            chat_area.config(state=tk.DISABLED)
            context_var.set(context_var.get() + f"\nUser: {user_input}\nAI: {result}")
            entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Chatbot")

    chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, width=100)
    entry.pack(padx=10, pady=10)
    entry.bind("<Return>", on_enter_pressed)

    context_var = tk.StringVar(value="")

    root.mainloop()


if __name__ == "__main__":
    handle_conversation()
