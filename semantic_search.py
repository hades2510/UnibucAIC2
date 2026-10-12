from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer(
  "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
texte = ["Un câine aleargă", "Un animal fuge", "Sortarea rapidă"]
v = model.encode(texte)
print(cosine_similarity(v[:1], v[1:]))
