import unittest
from text_process import TextHandler


class UnitTestsTextHandler(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTestsTextHandler, self).__init__(*args, **kwargs)
        self.handler = TextHandler()

    def test_get_line_words(self):
        words = self.handler._get_line_words('First check of this test')
        self.assertEqual(['First', 'check', 'of', 'this', 'test'], words)
        self.assertEqual(self.handler._word_half, None)

        words = self.handler._get_line_words('Second che-')
        self.assertEqual(['Second'], words)
        self.assertEqual(self.handler._word_half, 'che')

        words = self.handler._get_line_words('ck of this test')
        self.assertEqual(['check', 'of', 'this', 'test'], words)
        self.assertEqual(self.handler._word_half, None)

        words = self.handler._get_line_words('last check')
        self.assertEqual(['last', 'check'], words)
        self.assertEqual(self.handler._word_half, None)

    def test_add_char(self):
        self.handler._add_char('a')
        self.assertEqual(self.handler._characters, {'a': True})

        self.handler._add_char('b')
        self.assertEqual(self.handler._characters, {'a': True, 'b': True})

        self.handler._add_char('a')
        self.assertEqual(self.handler._characters, {'a': False, 'b': True})

        self.handler._add_char('c')
        self.assertEqual(self.handler._characters, {'a': False, 'b': True, 'c': True})

        self.handler._characters = dict()

    def test_get_first_unique_in_text(self):
        self.handler._add_char('a')
        self.handler._add_char('b')
        self.handler._add_char('c')
        self.handler._add_char('d')
        self.handler._add_char('a')
        self.handler._add_char('b')
        self.handler._add_char('d')
        self.handler._add_char('f')

        char = self.handler._get_first_unique_in_text()
        self.assertEqual(char, 'c')

        self.handler._characters = dict()

    def test_get_first_word_unique_char(self):
        char = self.handler._get_first_word_unique_char('hello')
        self.assertEqual(char, 'h')

        char = self.handler._get_first_word_unique_char('anna')
        self.assertEqual(char, None)

        char = self.handler._get_first_word_unique_char('Anna')
        self.assertEqual(char, 'A')

        char = self.handler._get_first_word_unique_char('proposition')
        self.assertEqual(char, 'r')

    def test_process_file(self):
        char = self.handler.process_file('tests/res/example.txt')
        self.assertEqual(char, 'm')

        char = self.handler.process_file('tests/res/text_without_unique_char.txt')
        self.assertEqual(char, None)

    def test_process_text(self):
        char = self.handler.process_text("""
The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"
        """)
        self.assertEqual(char, 'm')

        char = self.handler.process_text('hello, this texT has no unique character')
        self.assertEqual(char, None)


if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(UnitTestsTextHandler))

    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)