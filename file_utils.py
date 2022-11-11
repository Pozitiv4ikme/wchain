class FileUtils:
    @staticmethod
    def get_input_info(file_name: str = 'wchain.in') -> tuple[int, list[str]] | None:
        """
        read input info from given file
        :param file_name: file with input info
        :returns tuple with:
            - number of words;
            - list of all words;
        """
        with open(file_name, "r") as input_info:
            number_of_words = int(input_info.readline())
            words = []
            for word in input_info.readlines():
                words.append(word.strip())

        return number_of_words, words

    @staticmethod
    def put_result_info(info: int, file_name: str = 'wchain.out') -> None:
        """
        write output info into given file
        :param file_name: given file
        :param info: info to write into given file
        :return None:
        """
        with open(file_name, "w") as output_info:
            output_info.write(str(info))
