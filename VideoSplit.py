import os

def main():
    print("dddd")
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp4":
            print("processing", f)
            process(f)
        
def process(f):
    i=1
    inFile = f
    outFile = f[:-3]+"mp3"
    #cmd = "ffmpeg -i {} -vn -ac 2 -ar 44100 -ab 320k -f mp3 {}".format(inFile,outFile)
    #cmd = "ffmpeg -i -ss 00:00:03 -t 00:00:08 -async 1 cuti.mp4".format(inFile,outFile)
    #based on the length of video
    cmd = "ffmpeg -i output5.mp4 -c copy -map 0 -segment_time 00:02:00 -f segment -reset_timestamps 1 output%03d.mp4"


    os.popen(cmd)


main()