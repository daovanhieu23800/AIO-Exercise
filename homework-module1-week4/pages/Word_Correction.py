import streamlit as st


@st.cache_data
def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def levenshtein_distance(source: str, target: str) -> int:
    """Metric to calculate the difference between 2 string. This metric will calculate the minimum changes of source so that source == target"""
    result = 0

    matrix = [[0] * (len(target)+1) for _ in range(len(source)+1)]

    for i in range(len(source)+1):
        matrix[i][0] = i
    for i in range(len(target)+1):
        matrix[0][i] = i

    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i]
                                   [j-1], matrix[i-1][j]) + 1

    result = matrix[len(source)][len(target)]

    return result


def main():
    """main function"""
    st.set_page_config(
        page_title="Word Correction",
        page_icon="❌",
    )

    st.write("# Welcome to my Word Correction! ❌")

    vocabs = load_vocab(file_path='./source/data/vocab.txt')

    word = st.text_input('Input Word:')

    if st.button("Compute"):

        leven_distances = {}
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word:', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distances)

    st.sidebar.success("Select a project demo on the left side.")


if __name__ == "__main__":
    main()
