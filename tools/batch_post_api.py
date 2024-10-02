import os

input_dir = 'data/日向翔陽'
output_dir = 'data/日向翔陽_f'

for root, dirs, files in os.walk(input_dir):
    lab_files = [file for file in files if file.endswith('.lab')]
    total = len(lab_files)
    for i, lab_file in enumerate(lab_files):
        ref_wav_path = os.path.join(root, lab_file.replace('.lab', '.wav'))
        output_wav_path = os.path.join(output_dir, lab_file.replace('.lab', '_f'))
        text = open(os.path.join(root, lab_file)).read().strip()
        print(f'Processing {i+1}/{total}')
        # 呼叫 post_api.py 推理
        cmd = f'python -m tools.post_api --text "{text}" --reference_audio "{ref_wav_path}" --reference_text "{text}" --output "{output_wav_path}" --format "wav"'
        print(cmd)
        os.system(cmd)