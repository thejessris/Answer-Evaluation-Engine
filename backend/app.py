from fastapi import FastAPI
from pydantic import BaseModel

from extractor import extract_concepts
from scorer import score_concept
from feedback import generate_feedback

app = FastAPI(
    title="Answer Evaluation Engine"
)

class EvaluationRequest(BaseModel):

    question:str
    answer:str

@app.post("/evaluate")
def evaluate(req:EvaluationRequest):

    concepts = extract_concepts(
        req.question
    )

    concept_scores = []

    total_score = 0

    for concept in concepts:

        similarity = score_concept(
            concept,
            req.answer
        )

        marks = round(similarity * 2)

        total_score += marks

        concept_scores.append({
            "concept": concept,
            "score": marks,
            "similarity": similarity,
            "feedback": generate_feedback(
                similarity
            )
        })

    return {
        "total_score": total_score,
        "concept_scores": concept_scores
    }
