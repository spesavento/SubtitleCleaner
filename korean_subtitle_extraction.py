import webvtt

vtt_file = "./subtitle_files/Avatar_S01E03.vtt"
txt_file = "./clean_files/Avatar_S01E03.txt"

with open(txt_file, 'w') as f:
    for caption in webvtt.read(vtt_file):
        # print(caption.start)
        # #print(caption.end)
        # print(caption.text)
        f.write('\n')
        f.write(caption.text)

