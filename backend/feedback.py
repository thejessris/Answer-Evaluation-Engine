def generate_feedback(score):

    if score >= 0.8:
        return "Covered"

    elif score >= 0.5:
        return "Partially Covered"

    return "Missing"
