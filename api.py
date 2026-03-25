from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Music Sequencer API is running"}

@app.get("/generate")
def generate_music():
    try:

        subprocess.run(
            ["gcc", "A2_interactive_driver.c", "-o", "music"],
            check=True
        )

        input_commands = "6\nscherzino.txt\n7\n10\n"

        subprocess.run(
            ["./music"],
            input=input_commands,
            text=True,
            check=True
        )

        if os.path.exists("output.wav"):
            return FileResponse(
                path="output.wav",
                media_type="audio/wav",
                filename="output.wav"
            )
        else:
            return {"status": "error", "message": "wav not generated"}

    except Exception as e:
        return {"status": "error", "message": str(e)}