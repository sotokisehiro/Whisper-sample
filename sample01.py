import time
from faster_whisper import WhisperModel

# 実行前に、あらかじめ次のコマンドでモデルを変換しておくこと
# ct2-transformers-converter --model openai/whisper-large-v2 --output_dir whisper-large-v2-ct2     --copy_files tokenizer.json --quantization int8
model_size = "whisper-large-v2-ct2"

# CPUで使用する場合はdeviceに「cpu」と記述する
model = WhisperModel(model_size, device="cpu", compute_type="int8")

# CUDAが使用できる場合はdeviceに「cuda」と記述する
# model = WhisperModel(model_size, device="cuda", compute_type="int8")

# segments, info = model.transcribe("samples/jfk.wav")
segments, info = model.transcribe("samples/diffusion2023-07-03.wav")

print("Detected language '%s' with probability %f" %
      (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
