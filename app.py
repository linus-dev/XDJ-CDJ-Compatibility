import sys, getopt
import os
import mutagen

def main(argv):
    try:
        dir_path = argv[1]
    except:
        dir_path = os.path.dirname(os.path.realpath(__file__))

    if os.path.isdir(dir_path):
        unsupportedFiles = []

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".flac") or file.endswith(".mp3"):
                    print(file)
                    f = mutagen.File(os.path.join(root, file))

                    bitrate = f.info.bitrate / 1000
                    sample_rate = f.info.sample_rate

                    if sample_rate > 41000:
                        unsupportedFiles.append(file)
                    
        with open(os.path.dirname(os.path.realpath(__file__)) + '/unsupported_files.txt', 'w') as f:
            for item in unsupportedFiles:
                f.write("%s\n" % item)
    else:
        print("Directory not found.")
        sys.exit(2)

if __name__ == "__main__":
   main(sys.argv)