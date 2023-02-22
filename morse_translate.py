class MorseTranslate:
    morse_table = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '----': 'ch',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
    }

    @staticmethod
    def str_to_morse(
        text: str,
        char_delim: str = '|',
        word_delim: str = '||',
    ) -> str:
        if len(text) == 0:
            return ''
        result = ''
        words = text.split()
        for word in words:
            offset = 0
            for i in range(len(word)):
                i += offset
                if i >= len(word):
                    break
                char = word[i]
                if i - 1 < len(word):
                    if word[i:i + 2].lower() == 'ch':
                        char = 'ch'
                        offset += 1
                result += ''.join(
                    [
                        x[0] for x in MorseTranslate.morse_table.items()
                        if x[1] == char.lower()
                    ],
                )
                if i < len(word) - 1:
                    result += char_delim
            result += word_delim
        return result.strip(word_delim)

    @staticmethod
    def morse_to_str(
        morse: str,
        char_delim: str = '|',
        word_delim: str = '||',
    ) -> str:
        if len(morse) == 0:
            return ''
        result = ''
        words = morse.split(word_delim)
        for word in words:
            if len(word) > 0:
                chars = word.split(char_delim)
                for char in chars:
                    if len(char) > 0:
                        result += MorseTranslate.morse_table[char]
                result += ' '
        return result.strip()


def main() -> int:
    print(MorseTranslate.str_to_morse('funguje to'))
    print(MorseTranslate.morse_to_str('..-.|..-|-.|--.|..-|.---|.||-|---'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
