def collect_feedback(answer, user_feedback):
    """
    Collect feedback from the user about the answer.

    Args:
        answer (str): The generated answer.
        user_feedback (str): The user's feedback.

    Returns:
        dict: Collected feedback data.
    """
    return {"answer": answer, "feedback": user_feedback}
