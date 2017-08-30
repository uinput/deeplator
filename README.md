# About
Deeplator is a Python library and application enabling translation via [deepl.com](https://www.deepl.com/translator).

In August 2017, DeepL released the DeepL translator.
With unprecedented translation quality, the DeepL translator sets a new standard in neural machine translation.
Visit [deepl.com](https://www.deepl.com/press.html) to get more information.

# Usage
Using the application is straight forward.
The `-l` argument specifies the source and output languages.
Use the format AA-BB where AA ist the source language and BB is the output language.
For example, if you were to translate from English to German, the argument should be `-l EN-DE`.

You can tell Deeplator to read input from a file using the `-f` argument.
When ommitted, Deeplator will read input from `stdin` instead.
Remember to exit the multiline input with `Ctrl+D`.

# Dependencies
- Requests
