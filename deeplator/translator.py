from .jsonrpc import JSONRPCBuilder

POST_URL = "https://www.deepl.com/jsonrpc"
VALID_LANGS = ["EN", "DE", "FR", "ES", "IT", "NL", "PL"]


class Translator():
    def __init__(self, src_lang, dst_lang):
        self.src_lang = src_lang.upper()
        self.dst_lang = dst_lang.upper()

        if self.src_lang not in VALID_LANGS:
            raise ValueError("Input language not supported.")
        if self.dst_lang not in VALID_LANGS:
            raise ValueError("Output language not supported.")

    def split_into_sentences(self, text):
        if not text:
            return []

        method = "LMT_split_into_sentences"
        params = {
            "texts": [text.strip()],
            "lang": {
                "lang_user_selected": self.src_lang
            }
        }
        rpc = JSONRPCBuilder(method, params)
        resp = rpc.send(POST_URL)
        return resp["splitted_texts"][0]

    def translate_sentences(self, sentences):
        if not sentences:
            return []

        jobs = [{"kind": "default", "raw_en_sentence": s} for s in sentences]
        method = "LMT_handle_jobs"
        params = {
            "jobs": jobs,
            "lang": {
                "source_lang": self.src_lang,
                "target_lang": self.dst_lang
            }
        }
        rpc = JSONRPCBuilder(method, params)
        resp = rpc.send(POST_URL)
        translations = resp["translations"]
        extract = lambda obj: obj["beams"][0]["postprocessed_sentence"] if len(obj["beams"]) > 0 else '<empty-translation>'
        return [extract(obj) for obj in translations]

    def translate_sentence(self, sentence):
        if not sentence:
            return ""

        return self.translate_sentences([sentence])[0]
