#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from pathlib import Path

from deeplator import Translator, VALID_LANGS

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Deeplator is an application enabling translation via the DeepL translator."
    )
    parser.add_argument("-l", "--lang", dest="lang", type=str,
                        help="""The translation code used for translation.
                        Use the format AA-BB where AA is the source language
                        and BB is the output language. Example: EN-DE to
                        translate from English to German.""")
    parser.add_argument("-f", "--file", dest="path", type=Path,
                        help="Read input from specified file.")
    args = parser.parse_args()

    if args.lang:
        lang = args.lang.split("-")
        if len(lang) != 2:
            raise Exception("Invalid translation Code.")
    else:
        langs = ",".join(VALID_LANGS)
        print("You did not specify a translation code.")
        print("Available languages are {}.".format(langs))
        lang = []
        lang_tmp = str(input("Source language: "))
        lang.append(lang_tmp)
        lang_tmp = str(input("Output language: "))
        lang.append(lang_tmp)

    t = Translator(lang[0], lang[1])

    if args.path:
        with open(args.path, "r") as src_file:
            text = src_file.read()
    else:
        print("Enter the text to be translated. Use Ctrl+D to exit.")
        lines = sys.stdin.readlines()
        text = "".join(lines)
        print("-" * 16)

    sentences = t.split_into_sentences(text)
    translations = t.translate_sentences(sentences)
    for sentence in translations:
        print(sentence)
