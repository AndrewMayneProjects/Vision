import json

def count_correct_answers(file_path):
    correct_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            if data.get("correct") == "true":
                correct_count += 1
    return correct_count

# Paths to the JSONL files
modified_prompt_results_path = 'modified_prompt_results.jsonl'
paper_prompt_results_path = 'paper_prompt_results.jsonl'

# Counting correct answers
correct_answers_modified = count_correct_answers(modified_prompt_results_path)
correct_answers_paper = count_correct_answers(paper_prompt_results_path)

print(f"Correct answers in modified_prompt_results.jsonl: {correct_answers_modified}")
print(f"Correct answers in paper_prompt_results.jsonl: {correct_answers_paper}")
