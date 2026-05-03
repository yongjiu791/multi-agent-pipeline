# multi_agent_pipeline.py
from typing import List
import re

# 示例文本数据
RAW_DATA = [
    "AI is transforming the world. OpenAI develops powerful models.",
    "Agents can automate workflows and handle complex reasoning tasks.",
    "Python is great for prototyping multi-agent systems."
]

# ------------------------------
# Agent 1: Data Fetcher
# ------------------------------
class DataFetcher:
    def __init__(self, data_source: List[str]):
        self.data_source = data_source

    def fetch(self):
        # 模拟爬取数据
        print("[DataFetcher] Fetching raw data...")
        return self.data_source

# ------------------------------
# Agent 2: Text Cleaner
# ------------------------------
class TextCleaner:
    STOPWORDS = {"is", "the", "and", "for", "can"}

    def clean(self, texts: List[str]) -> List[str]:
        print("[TextCleaner] Cleaning texts...")
        cleaned = []
        for t in texts:
            t_lower = t.lower()
            t_no_punct = re.sub(r'[^\w\s]', '', t_lower)
            t_filtered = " ".join([w for w in t_no_punct.split() if w not in self.STOPWORDS])
            cleaned.append(t_filtered)
        return cleaned

# ------------------------------
# Agent 3: Keyword Extractor (long-chain reasoning)
# ------------------------------
class KeywordExtractor:
    def extract(self, texts: List[str]) -> List[List[str]]:
        print("[KeywordExtractor] Extracting keywords...")
        keywords_list = []
        for t in texts:
            words = t.split()
            # 长链推理示例：根据词频和长度选择关键词
            keywords = sorted(words, key=lambda w: (-len(w), w))[:5]
            keywords_list.append(keywords)
        return keywords_list

# ------------------------------
# Agent 4: Report Generator
# ------------------------------
class ReportGenerator:
    def generate(self, keywords_list: List[List[str]]):
        print("[ReportGenerator] Generating report...\n")
        for i, kws in enumerate(keywords_list, 1):
            print(f"Text {i} top keywords: {', '.join(kws)}")

# ------------------------------
# Pipeline Orchestration
# ------------------------------
class MultiAgentPipeline:
    def __init__(self):
        self.fetcher = DataFetcher(RAW_DATA)
        self.cleaner = TextCleaner()
        self.extractor = KeywordExtractor()
        self.reporter = ReportGenerator()

    def run(self):
        # Step 1: Fetch
        data = self.fetcher.fetch()
        # Step 2: Clean
        clean_data = self.cleaner.clean(data)
        # Step 3: Extract keywords (长链推理)
        keywords = self.extractor.extract(clean_data)
        # Step 4: Generate report
        self.reporter.generate(keywords)

if __name__ == "__main__":
    pipeline = MultiAgentPipeline()
    pipeline.run()