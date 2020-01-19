import numpy as np

from test_data_processor import get_test_data_frames, split_frames_by_is_valid
from train_data_processor import prepare_features_labels, create_features
from train_model import train_model

alphabet = ["A", "C", "G", "T"]
k = 4
train_filenames_labels = (("./data/vista1500", 1), ("./data/randoms1500", 0))
test_filename = "./data/chr21.fa"
frame_length = 1500
step = 750


def get_probabilities_for_1_list(valid_frames, invalid_frames, y_test_valid_proba):
    prob_for_1 = [0] * (len(valid_frames) + len(invalid_frames))
    
    for valid_frame_ind in range(len(valid_frames)):
        prob_for_1_ind = int(valid_frames[valid_frame_ind].begin / step)
        prob_for_1[prob_for_1_ind] = y_test_valid_proba[valid_frame_ind][1]

    mean_prob = np.mean(y_test_valid_proba[:, 1], axis=0)

    for invalid_frame_ind in range(len(invalid_frames)):
        prob_for_1_ind: int = int(invalid_frames[invalid_frame_ind].begin / step)
        prob_for_1[prob_for_1_ind] = mean_prob

    return np.array(prob_for_1)


def save_as_wig(filename, probabilities):
    new_shape = (len(probabilities), 1)
    indices = np.arange(new_shape[0]) * step + 1
    indices.dtype = "int64"
    indices = indices.reshape(new_shape)
    probabilities = probabilities.reshape(new_shape)
    data = np.concatenate((indices, probabilities), axis=1)
    np.savetxt(filename, data, fmt=["%d", "%.2f"])


if __name__ == "__main__":
    X_train, y_train = prepare_features_labels(train_filenames_labels, alphabet=alphabet, k=k)
    clf = train_model(X_train, y_train)

    test_frames = get_test_data_frames(test_filename, frame_length=frame_length, step=step)
    valid_frames, invalid_frames = split_frames_by_is_valid(test_frames)

    X_test = create_features(valid_frames,
                             alphabet=alphabet,
                             k=k)
    y_test_valid_proba = clf.predict_proba(X_test)
    y_test_all_proba = get_probabilities_for_1_list(valid_frames, invalid_frames, y_test_valid_proba)
    save_as_wig("./output/chr_prob.wig", y_test_all_proba)
