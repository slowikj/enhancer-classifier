from test_data_processor import get_test_data_frames, split_frames_by_is_valid
from train_data_processor import prepare_features_labels, create_features
from train_model import train

alphabet = ["A", "C", "G", "T"]
k = 4
train_filenames_labels = (("./data/vista1500", 1), ("./data/randoms1500", 0))
test_filename = "./data/chr21.fa"
frame_length = 1500
step = 750

if __name__ == "__main__":
    X_train, y_train = prepare_features_labels(train_filenames_labels, alphabet=alphabet, k=k)
    clf = train(X_train, y_train)

    test_frames = get_test_data_frames(test_filename, frame_length=frame_length, step=step)
    valid_frames, invalid_frames = split_frames_by_is_valid(test_frames)
    X_test = create_features(map(lambda frame: frame.sequence, valid_frames),
                             alphabet=alphabet,
                             k=k)
    y_test_proba = clf.predict_proba(X_test)
    print(y_test_proba)
