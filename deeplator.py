#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from pathlib import Path

from deeplator.translator import Translator

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Deeplator is an application enabling translation via deepl.com."
    )
    parser.add_argument("-l", "--lang", dest="lang", type=str, required=True,
                        help="""The language code used for translation.
                        Use the format AA-BB where AA is the source language
                        and BB is the output language. Example: EN-DE to translate
                        from English to German.""")
    parser.add_argument("-f", "--file", dest="path", type=Path,
                        help="Read input from specified file.")
    args = parser.parse_args()

    lang = args.lang.split("-")
    if len(lang) != 2:
        raise Exception("Invalid language Code.")

    if args.path:
        with open(args.path, "r") as src_file:
            text = src_file.read()
    else:
        print("Enter the text to be translated. Use Ctrl+D to exit.")
        lines = sys.stdin.readlines()
        text = "".join(lines)

    t = Translator(lang[0], lang[1])
    sentences = t.split_into_sentences(text)
    print(sentences)
    translations = t.translate_sentences(sentences)
    print(translations)
