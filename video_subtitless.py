"""from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Enter Video ID")
srt = YouTubeTranscriptApi.get_transcript(video_id)

subtitles_file = open('srt_file.txt', 'w')
for text in srt:
    subtitles_file.write(f"{text.get('text')}\n")"""
import requests

"""function validVideoId(id) {
		var img = new Image();
		img.src = "http://img.youtube.com/vi/" + id + "/mqdefault.jpg";
		img.onload = function () {
			checkThumbnail(this.width);
		}
	}

	function checkThumbnail(width) {
		//HACK a mq thumbnail has width of 320.
		//if the video does not exist(therefore thumbnail don't exist), a default thumbnail of 120 width is returned.
		if (width === 120) {
			alert("Error: Invalid video id");
		}
	}"""






"""# importing pafy
import pafy
	
# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"
	
# getting video
video = pafy.new(url)

# getting video ID
value = video.videoid

# printing the value
print("Video ID : " + value)
"""


"""
def validVideoId(video_id):  
	img = Image()
	img.src = "http://img.youtube.com/vi/" + video_id + "/mqdefault.jpg"
	img.onload = checkthumbnail('width')


def checkthumbnail(width):
	# HACK a mq thumbnail has width of 320.
	# if the video does not exist(therefore thumbnail don't exist), a default thumbnail of 120 width is rdeturned.
	if width == 120:
		messagebox.showerror("Error", "Invalid video id")
	else:
		messagebox.showinfo("Valid ID", "Video ID is valid")"""

r = requests.get("https://www.youtube.com/watch?v=nghuHvKLhJA") # random video id
print("Video unavailable" in r.text)






"""def video_subtitles():
    video_id = video_id_field.get()
    if video_id:
        srt = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles_file2 = open('srt_file1.txt', 'w')
        for text in srt:
            # subtitles_file2.write("%s\n" % text['text'])
            subtitles_file2.write(f"{text.get('text')}\n")
        messagebox.showinfo("Alert Message", "Video Transcript Downloaded")
    elif video_id == '':
        messagebox.showwarning("Error Message", "Please Enter Video ID ")
    else:
        messagebox.showwarning("Error Message", "Video does not exist ")"""







