from openai import OpenAI
import os, time
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"]
)
start = time.perf_counter()
r = client.chat.completions.create(
  model="qwen/qwen3-32b",
  messages=[{"role":"user", "content":"Explică BFS în 3 pași."}]
)
print(r.choices[0].message.content)
print("secunde:", time.perf_counter()-start)
