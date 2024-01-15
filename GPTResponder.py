import openai
from keys import OPENAI_API_KEY
from prompts import create_prompt, INITIAL_RESPONSE
import time
import re


openai.api_key = OPENAI_API_KEY

def generate_response_from_transcript(transcript):
    try:
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                messages=[{"role": "system", "content": create_prompt(transcript)}],
                temperature=0.0
        )
    except Exception as e:
        print(e)
        return '', ''
    
    full_response = response.choices[0].message.content

    print(full_response)

    # Split the response into brief and detailed parts
    try:
          # Use regular expressions to find the brief and detailed responses
        brief_match = re.search(r"\[Brief Answer\]:\s*(.*?)\n", full_response, re.IGNORECASE)
        detailed_match = re.search(r"\[Expanded Explanation\]:\s*(.*)", full_response, re.IGNORECASE | re.DOTALL)

        brief_response = brief_match.group(1) if brief_match else ''
        detailed_response = detailed_match.group(1).strip() if detailed_match else ''
        return brief_response, detailed_response
    except:
        return '', ''

    
class GPTResponder:
    def __init__(self):
        self.response = INITIAL_RESPONSE
        self.response_interval = 2

    def respond_to_transcriber(self, transcriber):
        while True:
            if transcriber.transcript_changed_event.is_set():
                start_time = time.time()

                transcriber.transcript_changed_event.clear() 
                transcript_string = transcriber.get_transcript()
                brief_response, detailed_response = generate_response_from_transcript(transcript_string)
                
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time  # Calculate the time it took to execute the function
                
                if brief_response:
                    self.response = f"Brief:\n {brief_response}\n\nDetailed:\n {detailed_response}"

                remaining_time = self.response_interval - execution_time
                if remaining_time > 0:
                    time.sleep(remaining_time)
            else:
                time.sleep(0.3)

    def update_response_interval(self, interval):
        self.response_interval = interval