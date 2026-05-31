from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def score_concept(concept, answer):

    concept_embedding = model.encode([concept])

    answer_embedding = model.encode([answer])

    similarity = cosine_similarity(
        concept_embedding,
        answer_embedding
    )[0][0]

    return round(float(similarity),2)
