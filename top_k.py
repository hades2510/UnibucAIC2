import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
  "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
texts = [r["text"] for r in records]
vectors = model.encode(texts, normalize_embeddings=True)
query = model.encode(["curaj și perseverență"], normalize_embeddings=True)[0]
scores = vectors @ query
for i in np.argsort(scores)[-3:][::-1]:
    print(round(float(scores[i]), 3), texts[i])
