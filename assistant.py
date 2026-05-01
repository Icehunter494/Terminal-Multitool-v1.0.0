import ollama
from duckduckgo_search import DDGS


def web_search(query):
    print(f"Searching the web for: {query}...")
    with DDGS() as ddgs:
        #gets top 3 results
        results = [r['body'] for r in ddgs.text(query, max_results=3)]
    return "\n".join(results)
def run():
    print("\n--- Local AI Assistant (Web-Enabled) ---")
    while True:
        user_input = input("\nYou: ").lower()
        if user_input in ["exit", "back"]: break


        search_data = web_search(user_input)

        print("Thinking...")
        response = ollama.chat(model='phi3', messages=[
            {'role': 'system', 'content': f'You are a helpful assistant. Use this web data to answer the user: {search_data}'},
            {'role': 'user', 'content': user_input},
            ])
        
        print(f"\nAssistant: {response['message']['content']}")