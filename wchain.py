class Wchain:
    @staticmethod
    def find_maximum_chain(words_list: str) -> tuple[int, list[str]]:
        """
        find the maximum chain of words from input
        list of words
        :param words_list: list of words
        :return the length of maximum chainx:
        """

        # we sort the incoming list in order to reduce the difficulty of searching for a word in the future
        words = sorted(words_list, key=len)

        # initialize the dictionary where we will record the length of the chain formed from word that we pass as a key
        length_of_chains_words = {word: 1 for word in words}

        # initialize the dictionary where we will write words that can be formed from the word passed as a key
        chains_of_words_dict = {word: [word] for word in words}

        for word in chains_of_words_dict.keys():
            # if the word consists of one letter, we skip this iteration, since there is nothing to cross out
            if len(word) == 1:
                continue

            # we check what words can be formed from this word and whether they exist in our input list of words
            for index in range(len(word)):

                # we form a new word by removing one letter
                new_word = word.replace(word[index], '', 1)

                if new_word in words:

                    # we check whether the chain for the formed word is larger than the already existing one
                    if length_of_chains_words[new_word] + 1 > length_of_chains_words[word]:
                        length_of_chains_words[word] = length_of_chains_words[new_word] + 1
                        chains_of_words_dict[word] += chains_of_words_dict[new_word]

        maximum_chain_length: int = max(length_of_chains_words.values())
        result_word_chain_index = words[list(length_of_chains_words.values()).index(maximum_chain_length)]
        result_word_chain = chains_of_words_dict[result_word_chain_index]

        return maximum_chain_length, result_word_chain
