import json

modified_samples = 0
original_samples = 0
def count_correct_answers(file_path):
    global modified_samples
    global original_samples
    
    correct_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            
            if "modified" in file_path:
                modified_samples += 1
            else:
                original_samples += 1
            
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

print(f"Correct answers in modified_prompt_results.jsonl: {correct_answers_modified}/{modified_samples}")
print(f"Correct answers in paper_prompt_results.jsonl: {correct_answers_paper}/{original_samples}")
