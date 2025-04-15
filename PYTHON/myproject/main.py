import openai
from typing import List
import os

class HeadingGenerator:
    def __init__(self, api_key: str):
        """ Initialize the heading generator with OpenAI API key """
        openai.api_key = api_key

    def generate_headings(self, subject: str, num_headings: int = 5, style: str = "engaging") -> List[str]:
        """ Generate creative headings based on the given subject

        Parameters:
        subject: The topic to generate headings for
        num_headings: Number of headings to generate
        style: Style of headings (engaging, professional, creative, etc.)

        Returns:
        List of generated headings
        """
        prompt = f"""Generate {num_headings} {style} headings for the following subject: {subject}
        The headings should be:
        - Attention-grabbing
        - Relevant to the subject
        - Between 5-10 words
        - Appropriate for the target audience
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional headline writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,  # Controls creativity level
                max_tokens=200
            )
            # Extract and clean headings from response content
            content = response.choices[0].message.content
            headings = [line.strip() for line in content.split('\n') if line.strip()]
            # Remove any numbering if present
            headings = [h.split('. ')[-1] for h in headings]
            return headings
        except Exception as e:
            print(f"Error generating headings: {str(e)}")
            return []

class SimpleHeadingUI:
    def __init__(self):
        """ Initialize the UI with a heading generator instance """
        # Get API key from environment variable
        api_key = "YOUR_API_KEY_HEREsk-proj-sGhyuqG32iH4NMjNe66LmjBUpPG2iYUceXXKr-eyCJlgKWFeOcZky-1wF8nbKWB4e6H08dQZmfT3BlbkFJk-zKiSLCPAcEH5AgqMi-Y0bQ_QLbHdycsyXUiqBQhQBpjX7I5IXEG1-JOLEEB8khW3aNko7AEA"  # Replace with your actual API key
        self.generator = HeadingGenerator(api_key)

    def run(self):
        """ Run the interactive heading generator interface """
        while True:
            print("\n=== AI Heading Generator ===")
            subject = input("Enter your subject (or 'quit' to exit): ")
            if subject.lower() == 'quit':
                break
            # Get additional parameters
            try:
                num_headings = int(input("How many headings do you want? (default: 5): ") or 5)
                style = input("What style do you want? (engaging/professional/creative) [default: engaging]: ") or "engaging"
                print("\nGenerating headings...")
                headings = self.generator.generate_headings(subject, num_headings, style)
                print("\nGenerated Headings:")
                for i, heading in enumerate(headings, 1):
                    print(f"{i}. {heading}")
            except ValueError as e:
                print(f"Error: {str(e)}")
                continue

# Example usage
if __name__ == "__main__":
    try:
        ui = SimpleHeadingUI()
        ui.run()
    except ValueError as e:
        print(f"Setup error: {str(e)}")