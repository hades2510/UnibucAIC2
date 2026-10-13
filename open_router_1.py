import os, requests
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"}
models = ["google/gemini-2.5-flash", "qwen/qwen3-32b"]
prompt = "Explică pe scurt de ce cerul este albastru."
for model in models:
    for trial in range(2):
        r = requests.post(url, headers=headers, timeout=90,
          json={"model":model,"messages":[{"role":"user","content":prompt}],
                "temperature":0.8})
        r.raise_for_status()
        print(model, trial, r.json()["choices"][0]["message"]["content"])
