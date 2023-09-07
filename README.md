# Whisper-sample
Linux/wslでインストール（仮想環境を推奨）
```
git clone https://github.com/sotokisehiro/Whisper-sample
cd Whisper-sample
pip install -r requirements.txt
ct2-transformers-converter --model openai/whisper-large-v2 --output_dir whisper-large-v2-ct2 \
     --copy_files tokenizer.json --quantization int8
mkdir samples
(samplesに適当なWAVファイルを「diffusion2023-07-03.wav」にrenameしてコピーしておく)
python sample01.py
```
