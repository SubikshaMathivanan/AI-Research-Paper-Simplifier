import yake

def extract_keywords(text):

    extractor = yake.KeywordExtractor()

    keywords = extractor.extract_keywords(text)

    return keywords[:10]