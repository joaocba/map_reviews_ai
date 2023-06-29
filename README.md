## Map Reviews using OpenAi

#### Technology: OpenAi
#### Method: Completions (gpt3.5 turbo model)

#### Description:
Script to map reviews using OpenAi completions, the purpose is to assign a new category to a review (based on a defined list of categories) that ingest the review data and return the review id and the new category id assigned to it.S

This script will read each row of a CSV file and output the mapped values (review id, category id) to a file.
It features OpenAi GPT 3.5 for a cheaper and faster process but to prevent API call exhaust it include a sleeper between calls.


### How to run (commands Windows terminal with Python 2.7):

#### Part One: Prepare Environment
- **Define necessary parameters (OpenAi API key, ...) on file 'app.py'**
- Initialize virtual environment and install dependencies, run:

	    virtualenv env
	    env\Scripts\activate
        pip install openai

#### Part Two: Define prompt to use

- Define the prompt to use on file '_shared.py' (this is encapsulated data to send via API with the data from CSV so OpenAi is aware of the task to run each time)

#### Part Three: Run the script

- To run the script:

	    python app.py

- It will start printing the mapped data as it read each row from the CSV, the prompt cache will be cleared every a few rows to avoid token limit exhaust so it can contiously read thousands of rows but still understand what it did before. The data will saved file 'output.txt'

#### OPTIONAL: Compare output mapped reviews with another file

- define the file 1 and file 2

		compare_files('./reviews_dir/output_compare.txt', './reviews_dir/manual_reviews_mapped.txt')

- To run the script:

	    python compare_files.py

- It will start printing the not matching review IDs from file 1 to file 2 and will also return a matching score from 0% to 100%

		Running Compare Reviews Script...

		Not matching: File 1: 4, 22 <#> File 2: 4, 4
		Not matching: File 1: 15, 1 <#> File 2: 15, 4
		Not matching: File 1: 17, 11 <#> File 2: 17, 23
		Not matching: File 1: 26, 13 <#> File 2: 26, 1
		Not matching: File 1: 32, 0 <#> File 2: 32, 13

		Matching score: 83.33%

#### Changelog
- v0.2
	- added a script to mapped reviews with manually mapped reviews and return a matching score (compare_files.py)
	- added a new function to keep some prompt history to not lose previous answers format when doing API calls (app.py)

- v0.1
	- initial build