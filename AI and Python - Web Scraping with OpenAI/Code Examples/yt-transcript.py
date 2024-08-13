from youtube_transcript_api import YouTubeTranscriptApi

video_id = '6Zl8vBkKAWQ'

script = YouTubeTranscriptApi.get_transcript(video_id)

print(script)

for line in script:
    print(line['text'])