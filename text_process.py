"""
Author: Kharkovnyk Artem.

Task: You need to develop an algorithm for a program that should do the following: - the program
accepts an arbitrary text as input and finds in each word of this text the very first symbol that
is NOT repeated in the analyzed word - further, from the received set of symbols, the program must
select the first unique one (that is, the one that is no longer found in the set) and return it.

For example, if the program receives the text below:

The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"

then it should return the character "m"
"""


import re
import argparse
from typing import Optional, Callable, Any, Type


class TextHandler:
    """Class to process text."""

    def __init__(self):
        """
        Initialize a new instance of TextHandler class.

        Attributes:
            words_pattern (re.Pattern): searching words pattern
            _characters (dict): dictionary where each key is first unique characters in each
                text word and boolean values which answer the question "Is key unique ?".
            _word_half (str): half of the word split in wto lines with  hyphen.

        """
        self._words_pattern = re.compile(r"([A-Za-z][A-Za-z-]*)")
        self._characters = {}
        self._word_half = None

    def _clean(
        method: Callable[[Type["TextHandler"], ...], Any]
    ) -> Callable[[Type["TextHandler"], ...], Any]:
        """
        Decorate method with adding class attributes post cleaning.
        """

        def method_with_post_cleaning(*args) -> Any:
            self = args[0]
            res = method(*args)
            self._characters = dict()
            self._word_half = None
            return res

        return method_with_post_cleaning

    def _get_line_words(self, line: str) -> list:
        """
        Give list of words written in 'line' argument.
        If line has word which ended with a hyphen, next method usage will join it with first
        word.
        Example:
            words1 = self._get_line_words('Hello everyone. Are you rea-')
            words2 = self._get_line_words('dy to work.')

            words1: ['Hello', 'everyone', 'Are', 'you']
            words2: ['ready', 'to', 'work']

        Args:
            line: string with words to get.

        Returns:
            List of words.
        """
        words = self._words_pattern.findall(line)
        if self._word_half is not None:
            words[0] = self._word_half + words[0]
        if words[-1][-1] == "-":
            self._word_half = words[-1][:-1]
            return words[:-1]
        else:
            self._word_half = None
            return words

    def _add_char(self, char: str) -> None:
        """
        Add character to the self._characters dictionary.

        Args:
            char: character to add to the self._characters dictionary.
        """

        if char in self._characters:
            self._characters[char] = False
        else:
            self._characters[char] = True

    def _get_first_unique_in_text(self) -> Optional[str]:
        """
        Give first unique character of set unique characters where or None if word has no
        unique character. Character searches in self._characters dictionary, which fills with
        self._add_char method. For correct work of this method previous fills self._characters
        dictionary is required.

        Returns:
            First unique character of set unique characters where or None if word has no unique
            character.

        """

        for char, unique in self._characters.items():
            if unique:
                return char
        return None

    def _get_first_word_unique_char(self, word: str) -> Optional[str]:
        """
        Search for the first unique character in a word.

        Args:
            word: word to process.

        Returns:
            First unique character or None if word has no unique character.

        Example:
            self._get_first_word_unique_char('hello')
        """
        characters = {}
        for char in word:
            if char in characters:
                characters[char] = False
            else:
                characters[char] = True
        for char, unique in characters.items():
            if unique:
                return char
        return None

    @_clean
    def process_text(self, text: str) -> Optional[str]:
        """
        Process text to find first unique character in set where characters are first unique in
        each text word.

        Args:
            text: text to process.

        Returns:
            First unique character of set unique characters where or None if word has no unique
            character.
        """
        words = self._get_line_words(text)
        for word in words:
            unique_char = self._get_first_word_unique_char(word)
            if unique_char is not None:
                self._add_char(unique_char)
        return self._get_first_unique_in_text()

    @_clean
    def process_file(self, filepath: str) -> Optional[str]:
        """
        Process text written in a file to find the first unique character in a set of characters
        where each character is first unique in each text word.


         Args:
            filepath: absolute or relative path to file.

        Returns:
            First unique character of set unique characters where or None if word has no unique
            character.
        """
        with open(filepath, "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if not line:
                    file.close()
                    return self._get_first_unique_in_text()
                words = self._get_line_words(line)
                for word in words:
                    unique_char = self._get_first_word_unique_char(word)
                    if unique_char is not None:
                        self._add_char(unique_char)


def main() -> None:
    """Script entrypoint."""
    parser = argparse.ArgumentParser(
        prog="text process",
        description="Program search first unique characters in each word and then search first \
                    unique in gotten data characters set",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--text", help="input text to process")
    group.add_argument("-f", "--file", help="file with text to process")
    args = parser.parse_args()
    handler = TextHandler()

    if args.text is not None:
        char = handler.process_text(args.text)
    else:
        char = handler.process_file(args.file)
    print(f"Result is: {char}")


if __name__ == "__main__":
    main()
