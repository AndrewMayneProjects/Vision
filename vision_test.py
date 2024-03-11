from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Set the number of times to run
num_runs = 100  # Dynamically set the number of runs

results = []  # List to store the results


modified_prompt = """There is a grid of 9 boxes, one of which is empty (marked as ?). You have to choose which of the 6 alternative shapes (A-F) should be placed in the empty box in order to complete the pattern that connects the shapes. Finally, provide your prediction as Answer: “X”.

- Describe the items in detail with specific attention on position.  
- Pay attention to simple details that might be different.
- Use a notation to hold your descriptions.
- Revisit your descriptions for consistency.
- Come up with a hypothesis.
- Create a test based on your hypothesis – don't simply agree with yourself. Run the test.
"""


prompt = """There is a grid of 9 boxes, one of which is empty (marked as ?). You have to choose which of the 6 alternative shapes (A-F) should be placed in the empty box in order to complete the pattern that connects the shapes. Finally, provide your prediction as Answer: “X”."""



image_url = "https://imagedelivery.net/sJGx3_sHkDXsn2q_3xlhLQ/1e5ff8bb-d259-4fd4-28bb-fe26203a5d00/portrait"


def isCorrect(text):
  
  text = text.strip()
  last_line = text.split("\n")[-1]
  print(last_line)
  if ("F" in last_line):
    return "true", last_line
  else:
    return "false", last_line

i = 1
correct_counter = 0

for _ in range(num_runs):
    print("Run ", i)
    response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": modified_prompt},
            {
              "type": "image_url",
              "image_url": {
                "url": image_url,
              },
            },
          ],
        }
      ],
      max_tokens=3000,
    )

    # Collect the prompt and output

    output = response.choices[0].message.content
    
    print(output)
    
    correctAnswer, last_line = isCorrect(output)
    
    if correctAnswer == "true":
      correct_counter += 1

    
    print(correct_counter, "out of", i)
    i += 1

    # Save the results to a JSONL file after each API call
    with open("modified_prompt_results_01_100.jsonl", "a") as outfile:
        json.dump({"correct": correctAnswer, "last_line": last_line, "prompt": prompt, "output": output, }, outfile)
        outfile.write('\n')  # Write a newline character to separate entries

print("Results saved to results.jsonl")