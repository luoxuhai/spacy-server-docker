from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import os

# Load the language model
MODEL = os.environ.get('LANGUAGE_MODEL', 'en_core_web_md')
nlp = spacy.load(MODEL, disable=["textcat"])
app = FastAPI()


class AnnotationParams(BaseModel):
    text: str


@app.post("/annotation")
def parse(params: AnnotationParams):
    doc = nlp(params.text)
    annotations = [
        {
            "text": token.text,
            "i": token.i,
            "idx": token.idx,
            "lemma": token.lemma_,
            # 较为简单的词性分类
            "pos": token.pos_,
            # 更具体的词性标签，它通常包括更多的信息和更精细的分类，NN（名词单数）
            "tag": token.tag_,
            "dep": token.dep_,
            "head": {
                "i": token.head.i,
                "idx": token.head.idx,
            },
            "is_punct": token.is_punct,
            "is_space": token.is_space,
            "ent_type": token.ent_type_,
            "ent_iob": token.ent_iob_,
        }
        for token in doc
    ]

    return {
        "annotations": annotations,
        "num_sentences": len(list(doc.sents))
    }


@app.get("/meta")
def read_root():
    return {
        "lang": nlp.meta['lang'],
        "name": nlp.meta['name'],
        "version": nlp.meta['version'],
        "spacy_version": spacy.__version__,
        "labels": nlp.meta.get('labels', None),
    }
