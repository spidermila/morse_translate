# morse_translate

Made for Czech language morse code. Import the MorseTranslate class and use it's static methods.

For example:
```python
from morse_translate import MorseTranslate

print(MorseTranslate.str_to_morse('funguje to'))
print(MorseTranslate.morse_to_str('..-.|..-|-.|--.|..-|.---|.||-|---'))
```

You can use different word and character delimiters, if needed.
