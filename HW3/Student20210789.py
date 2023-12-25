import os
import numpy as np

def load_data(folder):
    data = []
    labels = []
    for filename in os.listdir(folder):
        label = int(filename.split('_')[0]) 
        with open(os.path.join(folder, filename), 'r') as file:
            content = file.read().replace('\n', '')
            data.append([int(digit) for digit in content])
            labels.append(label)
    return np.array(data), np.array(labels)

def calculate_error(expected, labels):
    return np.mean(expected != labels) * 100

def knn(train_data, train_labels, test_data, test_labels, k):
    expected = []
    for test_item in test_data:
        distances = np.sum((train_data - test_item) ** 2, axis=1) ** 0.5
        nearest_neighbors = np.argsort(distances)[:k]
        nearest_labels = train_labels[nearest_neighbors]
        expected_label = np.argmax(np.bincount(nearest_labels))
        expected.append(expected_label)
    return calculate_error(np.array(expected), test_labels)

def main(training_folder, testing_folder):
    train_data, train_labels = load_data(training_folder)
    test_data, test_labels = load_data(testing_folder)
    
    for k in range(1, 21):
        error_rate = knn(train_data, train_labels, test_data, test_labels, k)
        print(f"{int(error_rate)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        sys.exit(1)
    
    training_folder = sys.argv[1]
    testing_folder = sys.argv[2]
    main(training_folder, testing_folder)
