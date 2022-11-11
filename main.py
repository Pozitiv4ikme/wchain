from file_utils import get_input_info, put_result_info


def main() -> int | None:
    """
    main function where we check input info and return result
    :return the length of the maximum chain:
    """
    n, words = get_input_info('wchain.in')

    if not (1 <= n <= pow(10, 5)):
        print("The number of words in the dictionary must be from 1 to 10^5")
        return

    for word in words:
        if not (1 <= len(word) <= 50):
            print("Word must be from 1 to 50 characters long")
            return
    return 0


if __name__ == '__main__':
    result = main()
    put_result_info('wchain.out', result)
