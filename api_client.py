import openai
import os
from dotenv import load_dotenv

class APIClient:
    def __init__(self):
        load_dotenv()
        api_key = os.environ.get('Your_API_Key')
        self.client = openai.OpenAI(api_key=api_key)

    def generate_summary_with_gpt3(self, points, combined_reviews):
        
        truncated_reviews = combined_reviews
        if points is None:
            prompt = "Please thoroughly review each of these hotel reviews and provide a summary. Ensure that the summary captures all the key information and highlights from the reviews." + truncated_reviews
        else:
            prompt = "Please transform each point from the provided comma-separated list into a concise sentence. Each sentence should elaborate on its respective point without deviating from its specific context or introducing additional information." + points

        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo",
        )

        # Extract and return the content from the response
        if chat_completion and chat_completion.choices:
            response_text = chat_completion.choices[0].message.content
            return response_text
        else:
            return "No response generated."
