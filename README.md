# Deeplator

## About
Deeplator is a Python library and application enabling translation via the DeepL translator available at [deepl.com](https://www.deepl.com/translator).

In August 2017, DeepL released the DeepL translator.
With unprecedented translation quality, the DeepL translator sets a new standard in neural machine translation.
Check out [deepl.com](https://www.deepl.com/press.html) to get more information.

Currently, the supported languages include English, German, French, Spanish, Italian, Dutch and Polish.

If you're coding in PHP instead, [DeepLy](https://github.com/chriskonnertz/DeepLy) might be the right choice.

## Application Usage
Using the application is straight forward.
Basically, you just need to launch `deeplator.py`.

The `-l LANG` argument specifies the source and output languages.
If omitted, the application will ask for the languages interactively.
`LANG` is the translation code in the format `AA-BB` where `AA` ist the source language code and `BB` is the output language code.
See the table below for all language codes.
For example, if you were to translate from English to German, the argument should be `-l EN-DE`.

|Language|Code|
|:-------|:--:|
|English |EN  |
|German  |DE  |
|French  |FR  |
|Spanish |ES  |
|Italian |IT  |
|Dutch   |NL  |
|Polish  |PL  |

You can tell Deeplator to read input from a file using the `-f PATH` argument.
When ommitted, Deeplator will read input from `stdin` instead.
Remember to exit the multiline input with `Ctrl+D`.

## Library Usage
The Deeplator library was written for Python 3.

### Single Sentence
```python
from deeplator import Translator

t = Translator("EN", "DE")
sentence = "Hello world."
translation = t.translate_sentence(sentence)
print(translation)
```

### Multiple Sentences
In case it is unknown if the input string consists of multiple sentences, use the `translate_sentences` method.
It will split the passed argument into sentences first and translate each sentence by its own.
```python
from deeplator import Translator

t = Translator("EN", "DE")
paragraph = "Hello world. DeepL is awesome."
translations = t.translate_sentences(paragraph)
print(translations)
```
