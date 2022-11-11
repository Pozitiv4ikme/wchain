from file_utils import FileUtils
from wchain import Wchain


def main() -> tuple[int, list[str]] | None:
    """
    main function where we check input info and return result
    :return the length of the maximum chain:
    """
    n, words = FileUtils.get_input_info()

    if not (1 <= n <= pow(10, 5)):
        print("The number of words in the dictionary must be from 1 to 10^5")
        return

    for word in words:
        if not (1 <= len(word) <= 50):
            print("Word must be from 1 to 50 characters long")
            return

    length_of_maximum_chain, word_chain = Wchain.find_maximum_chain(words)
    return length_of_maximum_chain, word_chain


if __name__ == '__main__':
    maximum_length, maximum_word_chain_representation = main()

    print(maximum_word_chain_representation)
    FileUtils.put_result_info(maximum_length)

