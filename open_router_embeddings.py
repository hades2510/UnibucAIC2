import os, requests, numpy as np
texts = ["Pisica doarme pe canapea", "Motanul se odihnește",
         "Am cumpărat un bilet de tren"]
r = requests.post("https://openrouter.ai/api/v1/embeddings",
  headers={"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"]},
  json={"model":"qwen/qwen3-embedding-8b", "input":texts}, timeout=90)
r.raise_for_status()
v = np.array([x["embedding"] for x in sorted(r.json()["data"], key=lambda x:x["index"])])
v = v / np.linalg.norm(v, axis=1, keepdims=True)
print(np.round(v @ v.T, 3))  # matrice de similaritate cosinu
