from urllib.error import URLError

from .jsonrpc import JSONRPCBuilder

POST_URL = "https://www.deepl.com/jsonrpc"
VALID_LANGS = ["EN", "DE", "FR", "ES", "IT", "NL", "PL"]
LENGTH_LIMIT = 5000


class Translator():
    def __init__(self, src_lang, dst_lang, check_length_limit=True):
        """The Translator class.

        :param src_lang: The source language.
        :param dst_lang: The output language.
        :param check_length_limit: whether to check strings for length or not.
        Default is ``True``.
        """

        self.src_lang = src_lang.upper()
        self.dst_lang = dst_lang.upper()

        if self.src_lang not in VALID_LANGS:
            raise ValueError("Input language not supported.")
        if self.dst_lang not in VALID_LANGS:
            raise ValueError("Output language not supported.")

        self.check_length_limit = check_length_limit

    def split_into_sentences(self, text):
        """
        Split a string into sentences using the DeepL API.

        :param text: A string to be split.
        :returns: A list of sentences with type string.
        :raises TranslationError: If there was an exception during the
        translation.
        """

        if not text:
            return []

        method = "LMT_split_into_sentences"
        params = {
            "texts": [text.strip()],
            "lang": {
                "lang_user_selected": self.src_lang
            }
        }

        resp = _send_jsonrpc(method, params)
        return resp["splitted_texts"][0]

    def translate_sentences(self, sentences):
        """
        Translate a list of single sentences or string of sentences into a list
        of translations. If a string was passed, it will be split into a list
        of sentences using the DeepL API first.

        :param sentences: A list of strings or string to be translated.
        :returns: A list of translated strings.
        :raises LengthLimitExceeded: If the length of a string exeeds the
        length limit of the DeepL API, an exception is raised.
        :raises TranslationError: If there was an exception during the
        translation.
        """

        # catch None, empty string and empty list
        if not sentences:
            return []
        elif type(sentences) is str:
            sentences = self.split_into_sentences(sentences)

        jobs = self._build_jobs(sentences)
        method = "LMT_handle_jobs"
        params = {
            "jobs": jobs,
            "lang": {
                "source_lang": self.src_lang,
                "target_lang": self.dst_lang
            }
        }

        resp = _send_jsonrpc(method, params)
        translations = resp["translations"]

        def extract(obj):
            if obj["beams"]:
                return obj["beams"][0]["postprocessed_sentence"]
            else:
                return EmptyTranslation()

        return [extract(obj) for obj in translations]

    def translate_sentence(self, sentence):
        """
        Translate a single sentence. Be aware that translation might be
        incorrect if a string with multiple sentences is passed. If unsure,
        use ``translate_sentences`` or split the string via
        ``split_into_sentences`` first.

        :param sentence: A string to be translated.
        :returns: The translated string.
        :raises LengthLimitExceeded: If the length of the string exeeds the
        length limit of the DeepL API, an exception is raised.
        :raises TranslationError: If there was an exception during the
        translation.
        """

        if not sentence:
            return ""

        return self.translate_sentences([sentence])[0]

    def _build_jobs(self, sentences):
        jobs = list()

        for s in sentences:
            if self.check_length_limit and len(s) > LENGTH_LIMIT:
                raise LengthLimitExceeded()
            else:
                job = {"kind": "default", "raw_en_sentence": s}
                jobs.append(job)

        return jobs


def _send_jsonrpc(method, params):
    try:
        rpc = JSONRPCBuilder(method, params)
        return rpc.send(POST_URL)
    except URLError as e:
        raise TranslationError(e.reason)


class LengthLimitExceeded(Exception):
    pass


class TranslationError(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __repr__(self):
        return "TranslationError: " + self.reason


class EmptyTranslation():
    def __repr__(self):
        return "<EmptyTranslation>"
