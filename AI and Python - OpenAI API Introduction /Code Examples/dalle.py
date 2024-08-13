from openai import OpenAI

client = OpenAI()

query = 'a dog on the moon'

response = client.images.generate(
  model="dall-e-3",
  prompt=query,
  n=1, #How many images to return
  size="512x512" #256x256, 512x512, 1024x1024
)
print(response)
print('')
print(response.created)
print('')
print(response.data[0].revised_prompt)
print('')
print(response.data[0].url)
