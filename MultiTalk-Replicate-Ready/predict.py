
import os
from cog import BasePredictor, Input, Path
import subprocess

class Predictor(BasePredictor):
    def setup(self):
        os.makedirs("outputs", exist_ok=True)

    def predict(
        self,
        audio: Path = Input(description="Input audio file (wav format)"),
        reference_image: Path = Input(description="Reference image of the speaker"),
        transcript: str = Input(description="Optional transcript", default=""),
    ) -> Path:
        output_path = "outputs/output.mp4"

        command = [
            "python3",
            "generate_multitalk.py",
            "--input_audio", str(audio),
            "--reference_image", str(reference_image),
            "--output_path", output_path,
        ]

        if transcript:
            command.extend(["--transcript", transcript])

        subprocess.run(command, check=True)
        return Path(output_path)
