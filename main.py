from engine.query_parser import parse_query
from engine.reasoning import reason
from engine.answer_generator import generate_answer

def main():
    user_query = input("Enter your research query: ")
    parsed_query = parse_query(user_query)
    reasoning_steps = reason(parsed_query)
    answer = generate_answer(reasoning_steps)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
