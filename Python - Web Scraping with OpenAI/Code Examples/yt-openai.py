from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

client = OpenAI()

# openai_key ='API Key from OpenAI'
# client = OpenAI(api_key=openai_key)

def transcript(video_id):
    script = YouTubeTranscriptApi.get_transcript(video_id)
    return script

def ai(query, text):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"provide answer from this document {text}"},
        {"role": "user", "content": query}
    ]
    )
    response = completion.choices[0].message.content
    return response

video_id = '6Zl8vBkKAWQ'
query = 'Tell me what general sections there are in this video'

result_text = transcript(video_id)
result_ai = ai(query, result_text)

print(result_ai)