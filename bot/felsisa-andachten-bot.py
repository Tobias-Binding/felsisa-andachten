# Imports
from youtube_video_upload import upload_video

client_id = '590400683231-lr5l9hev0h6mm6fuoceedd0085pmdoeh.apps.googleusercontent.com'
client_secrent = 'n156DPlMQa4F6_-M_jnMROSc'

# This function can take an audio file with a image and upload it to youtube.
credentials = 'credentials'
file = 'video.mp4'
upload_video(credentials,
        file,
        title='video title',
        description='video description',
        category=22,
        privacy='private',
        tags=[])


# Upload mp4 to youtube.
def mp4_to_youtube(mp4_file, name, description):
    print("Uploading {} to youtube with name: {} and description: {} ".format(mp4_file, name, description))

    return ()

# If mp4 file is given, ask for name and description and upload to youtube


# if mp3 (or other Audio file is given ask for Image, name , and description and upload to youtube)