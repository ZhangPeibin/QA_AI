
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-ykKYkD4LqX7jyLF0CnAJla3L"
openai.api_key = os.getenv("OPENAI_API_KEY")
# modelList = openai.Model.list()
# print(modelList)

response = openai.Completion.create(
  model='text-davinci-003',
  prompt='主题: 早餐 风\n两句话的恐怖故事:',
  temperature=0.8,
  max_tokens=120,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
)


print(response)