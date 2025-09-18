from flask import Flask, render_template
# from minio import Minio  # Comment out MinIO imports
# from minio.error import S3Error
# from datetime import timedelta
import os

app = Flask(__name__)

# Setup MinIO client using environment variables
# minioClient = Minio(
#     endpoint=os.getenv('MINIO_ENDPOINT'),
#     access_key=os.getenv('MINIO_ACCESS_KEY'),
#     secret_key=os.getenv('MINIO_SECRET_KEY')
# ) # Comment out the client setup

@app.route('/')
def index():
    # try:
    #     # List all objects in the bucket
    #     objects = minioClient.list_objects("music-bucket", recursive=True)
    #     music_files = []
    #     for obj in objects:
    #         # Generate a presigned URL for each music file
    #         url = minioClient.presigned_get_object("music-bucket", obj.object_name, expires=timedelta(hours=1))
    #         music_files.append((obj.object_name, url))
    
    # --- NEW CODE: Create a dummy list of music files ---
    music_files = [
        ("Dummy Song 1.mp3", "#"),
        ("Dummy Song 2.mp3", "#"),
        ("Another Track.mp3", "#")
    ]
    # --- END NEW CODE ---
    
    return render_template('index.html', music_files=music_files)

    # except S3Error as exc:
    #     print("Error occurred.", exc)
    #     return "Error in fetching music files", 500

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
