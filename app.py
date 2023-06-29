"""
Steps to run (python 2.7):
- virtualenv env
- env\Scripts\activate
- pip install openai
- python app.py

The output file will be generated inside the "reviews_dir" folder
The prompt intructions can be found on "_shared.py" file, if you change the system_prompt in use make sure you alter it on line 16 and line 32 to corresponding name
"""

import openai
import csv
import random
import time
from _shared import SYSTEM_PROMPT8_2


## CONFIG ##
# Set openai API key
openai.api_key = ''

# Specify path to CSV file
source_csv = "./reviews_dir/job_reviews_30.csv"

# Use sleep between openai api calls, this may help reduce api stress usage
use_sleep = True
# define randomizer for miliseconds, 0.5 = 500 miliseconds
sleep_time = random.uniform(0.8, 1.4)

# Obtain system prompt to include on call
system_prompt = f"{SYSTEM_PROMPT8_2}"
pre_prompt = [
    {
        "role": "system",
        "content": system_prompt,
    },
]
MAX_TOKENS = 100  # max amount of tokens in the prompt and response
# a defined number of messages to be processed before prompt is cleaned up
PROMPT_MESSAGE_LIMIT = 10


def map_category_ai(review_data, pre_prompt):
    """
    Maps a category to each review in the specified CSV file using OpenAI completions.

    :param review_data: The data from a row of a CSV file.
    :param pre_prompt: The defined prompt for the api call.
    """

    # Add review data to prompt
    pre_prompt.append({"role": "user", "content": review_data})

    # Retrieve response from openai API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            temperature=0.1,
            messages=pre_prompt,
            max_tokens=MAX_TOKENS,
            top_p=0.1
        )
    except openai.error.APIError as e:
        print(f"An error occurred while generating response for review: {e}")
        response = None

    # Add response to prompt
    if response is not None and len(response.choices) > 0:
        pre_prompt.append(
            {"role": "assistant", "content": response['choices'][0]['message']['content']})
        print(response['choices'][0]['message']['content'])
        with open("./reviews_dir/output.txt", "a+") as log_file:
            log_file.write(response['choices'][0]['message']['content']+"\n")
    else:
        pre_prompt.append(
            {"role": "assistant", "content": "Sorry, I could not generate a response."})


def reset_pre_prompt(pre_prompt):
    """
    Clears the prompt after processing a defined number of messages

    :param pre_prompt: The prompt to be cleaned.
    :return: A clean prompt.
    """
    pre_prompt = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]
    return pre_prompt


def clean_pre_prompt(pre_prompt):
    """
    Clears the prompt after processing a defined number of messages
    but keep the first message from system and the last two messages from user and assistant

    :param pre_prompt: The prompt to be cleaned.
    :return: A clean prompt.
    """
    clean_prompt = [
        {
            "role": "system",
            "content": pre_prompt[0]["content"],
        }
    ]
    if len(pre_prompt) > 4:
        clean_prompt += pre_prompt[-4:]
    else:
        clean_prompt += pre_prompt[1:]
    return clean_prompt


def get_csv_row_count(source_csv):
    """
    Retrieves the total number of rows in a CSV file.

    :param source_csv: The path to the CSV file.
    :return: The total number of rows in the CSV file, or -1 if an error occurs.
    """
    try:
        with open(source_csv, "r", encoding='utf-8-sig') as csv_file_count:
            csv_reader = csv.reader(csv_file_count)
            next(csv_reader)  # skip CSV header row
            csv_row_count = len(list(csv_reader))
        return csv_row_count
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return -1


def main():
    print("\nRunning Map Reviews Script...")

    csv_row_count = get_csv_row_count(source_csv)
    if csv_row_count == -1:
        return

    print("\nMapping", csv_row_count, "reviews")

    # Read CSV file
    with open(source_csv, "r", encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # skip CSV header row
        pre_prompt = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        print("\nReview ID | New Category ID")
        # Iterate through each row
        for i, row in enumerate(csv_reader):
            try:
                # Get the review data from the current row
                review_data = row[0]

                # Map the category using OpenAI completions
                map_category_ai(review_data, pre_prompt)
                #print(pre_prompt)

                # Sleep to avoid stressing the OpenAI API
                if use_sleep:
                    time.sleep(sleep_time)

                # Clean up the prompt after processing a defined number of messages
                if (i + 1) % PROMPT_MESSAGE_LIMIT == 0:
                    #pre_prompt = reset_pre_prompt(pre_prompt)
                    pre_prompt = clean_pre_prompt(pre_prompt)
                    print("\nPrompt messages cleaned!\n")
                    #print(pre_prompt)
            except Exception as e:
                print(f"Error occurred while mapping review {i + 1}: {e}")

    print("\nMapping complete! - Verify output file")


if __name__ == "__main__":
    main()
