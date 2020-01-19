from frame import Frame


def get_test_data_frames(file_path, frame_length, step):
    sequence = read_test_data_seq(file_path)
    frames = [Frame(sequence=sequence[beg: (beg + frame_length)], begin=beg)
              for beg in range(0, len(sequence) - frame_length, step)]
    return frames


def split_frames_by_is_valid(frames):
    return (
        filter(lambda f: f.is_valid, frames),
        filter(lambda f: not f.is_valid, frames)
    )


def read_test_data_seq(file_path):
    file_str = ""
    with open(file_path, "r") as f:
        f.readline()  # we omit the first line, because the data is in FASTA format
        for line in f:
            file_str += line[:-1]
    return file_str
