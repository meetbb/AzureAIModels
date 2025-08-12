import json
from dataclasses import dataclass
from typing import Any, List

# --------- Dataclass Definitions ---------
@dataclass
class ConfidenceScores:
    positive: float
    neutral: float
    negative: float

    @staticmethod
    def from_dict(obj: Any) -> 'ConfidenceScores':
        return ConfidenceScores(
            positive=float(obj.get("positive")),
            neutral=float(obj.get("neutral")),
            negative=float(obj.get("negative"))
        )

@dataclass
class Sentence:
    text: str
    sentiment: str
    confidenceScores: ConfidenceScores

    @staticmethod
    def from_dict(obj: Any) -> 'Sentence':
        return Sentence(
            text=str(obj.get("text")),
            sentiment=str(obj.get("sentiment")),
            confidenceScores=ConfidenceScores.from_dict(obj.get("confidenceScores"))
        )

@dataclass
class Document:
    id: str
    language: str
    sentiment: str
    confidenceScores: ConfidenceScores
    sentences: List[Sentence]

    @staticmethod
    def from_dict(obj: Any) -> 'Document':
        return Document(
            id=str(obj.get("id")),
            language=str(obj.get("language")),
            sentiment=str(obj.get("sentiment")),
            confidenceScores=ConfidenceScores.from_dict(obj.get("confidenceScores")),
            sentences=[Sentence.from_dict(s) for s in obj.get("sentences", [])]
        )

@dataclass
class Root:
    documents: List[Document]
    errors: List[Any]
    modelVersion: str

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        return Root(
            documents=[Document.from_dict(d) for d in obj.get("documents", [])],
            errors=obj.get("errors", []),
            modelVersion=str(obj.get("modelVersion"))
        )


# Load the local JSON file
def load_json_file(file_path: str) -> Root:
    """Load JSON and map to dataclasses."""
    with open("sample_response.json", "r") as file:
        data = json.load(file)

    return Root.from_dict(data)

print("\n--- Parsed Result ---")
api_response = load_json_file("sample_response.json")

for doc in api_response.documents:
    print(f"Document ID: {doc.id}")
    print(f"Language: {doc.language}")
    print(f"Overall Sentiment: {doc.sentiment}")
    print("Confidence Scores:")
    print(f"  Positive: {doc.confidenceScores.positive}")
    print(f"  Neutral:  {doc.confidenceScores.neutral}")
    print(f"  Negative: {doc.confidenceScores.negative}")
    
    print("Sentences:")
    for sentence in doc.sentences:
        print(f"    Text: {sentence.text}")
        print(f"    Sentiment: {sentence.sentiment}")
        print(f"    Positive: {sentence.confidenceScores.positive}")
        print(f"    Neutral:  {sentence.confidenceScores.neutral}")
        print(f"    Negative: {sentence.confidenceScores.negative}")
    print("-" * 40)