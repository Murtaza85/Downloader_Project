from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript('kqtD5dpn9C8')

f = open('srt_file.txt', 'w')
for i in srt:
    f.write('%s\n' % i)






