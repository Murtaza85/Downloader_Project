from youtube_transcript_api import YouTubeTranscriptApi


video_id = input("Enter Video ID")
srt = YouTubeTranscriptApi.get_transcript(video_id)



f = open('srt_file.txt', 'w')
for i in srt:
    f.write('%s\n' % i['text'])






