from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def extractive_summarization(text):
    # Parse the text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Use LSA Summarizer    
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=2)  # You can adjust the sentence count as needed

    # Combine the summary sentences into a single string
    summary_text = " ".join([str(sentence) for sentence in summary])

    return summary_text
