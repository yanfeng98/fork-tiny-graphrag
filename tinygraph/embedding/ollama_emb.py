from ollama import embed
from typing import List
from .base import BaseEmb

class ollamaEmb(BaseEmb):
    def __init__(self, model_name: str, **kwargs):
        super().__init__(model_name=model_name, **kwargs)

    def get_emb(self, text: str) -> List[float]:
        emb: list[float] = embed(model=self.model_name, input=text).embeddings[0]
        return emb, len(emb)

if __name__ == "__main__":

    # ollama pull nomic-embed-text
    emb = ollamaEmb(model_name="nomic-embed-text")
    # 768
    print(emb.get_emb("你好"))