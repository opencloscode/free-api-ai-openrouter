import json
import urllib.request

KEY = "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"
MODEL = "openrouter/free"
URL = "https://openrouter.ai/api/v1/chat/completions"

conversation_history = []

while True:
    msg = input("You: ")

    conversation_history.append({"role": "user", "content": msg})

    data = json.dumps({
        "model": MODEL,
        "messages": conversation_history
    }).encode("utf-8")

    req = urllib.request.Request(URL, data=data, headers={
        "Authorization": "Bearer " + KEY,
        "Content-Type": "application/json"
    })

    try:
        with urllib.request.urlopen(req) as r:
            result = json.loads(r.read().decode("utf-8"))

        ai_response = result["choices"][0]["message"]["content"]
        print("Ai:", ai_response)

        conversation_history.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print("Error:", e)
