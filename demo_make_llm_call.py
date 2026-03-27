from dotenv import load_dotenv
from google import genai
import re

load_dotenv()

client = genai.Client()


def generate_prompt():
    return """write the python code to calculate
a loan payment with the following inputs: interest,
term, present value. return code only wrapped in a Markdown
code block (triple backticks). Do not add any extra text or
explanation outside the code block."""


response = client.models.generate_content(
    model="gemini-2.5-flash", contents=generate_prompt()
)

match = re.search(r"```(?:python)?\s*([\w\W]*?)```", response.text, re.DOTALL)

if not match:
    raise ValueError("No code block found in Gemini response.")

code_content = match.group(1).strip()

print("---Extracted code ---")
print(code_content)

with open("loan_payment.py", "w", encoding="utf-8") as f:
    f.write(code_content)
