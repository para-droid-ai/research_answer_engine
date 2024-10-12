def parse_query(query):
    """
    Parse the natural language query to extract meaningful components.

    Args:
        query (str): The user's query.

    Returns:
        dict: Parsed components of the query.
    """
    parsed_query = {
        "intent": "research_query",
        "entities": extract_entities(query)
    }
    return parsed_query

def extract_entities(query):
    """
    Extract entities from the query.

    Args:
        query (str): The user's query.

    Returns:
        list: List of entities found in the query.
    """
    return ["entity1", "entity2"]
