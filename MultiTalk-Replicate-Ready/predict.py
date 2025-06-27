import os
import json
import subprocess
from cog import BasePredictor, Input, Path

class Predictor(BasePredictor):
    def setup(self):
        # ensure the outputs folder exists
        os.makedirs("outputs", exist_ok=True)

    def predict(
        self,
        audio: Path = Input(description="Input audio file (wav format or video)"),
        reference_image: Path = Input(description="Reference image of the speaker"),
    ) -> Path:
        input_dict = {
            "prompt": "",                          # no transcript in this setup
            "cond_image": str(reference_image),    # Cog has already downloaded it locally
            "cond_audio": {"person1": str(audio)}, # single-speaker
            "audio_type": "single"
        }
        json_path = "temp_input.json"
        with open(json_path, "w") as f:
            json.dump(input_dict, f)
        command = [
            "python3", "generate_multitalk.py",
            "--input_json", json_path,
            "--ckpt_dir",   "weights/Wan2.1-I2V-14B-480P",
            "--wav2vec_dir","weights/chinese-wav2vec2-base",
            "--save_file",  "outputs/output"
        ]
        subprocess.run(command, check=True)

        # 3) return the final MP4
        return Path("outputs/output.mp4")
