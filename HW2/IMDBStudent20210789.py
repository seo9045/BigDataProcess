import sys

def count_genre(input_f, output_f):
    genre_count = {}

    with open(input_f, 'r') as f:
        lines = f.readlines()

    for line in lines:
        movie_info = line.strip().split("::")
        genres = movie_info[2].split('|')
        for genre in genres:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

    with open(output_f, 'w') as f:
        for genre, count in genre_count.items():
            f.write(f"{genre} {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Rewrite")
    else:
        input_f = sys.argv[1]
        output_f = sys.argv[2]
        count_genre(input_f, output_f)
