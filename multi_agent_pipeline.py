# multi_agent_pipeline.py
from typing import List
import re

# 模拟原始文本数据
RAW_DATA = [
    "AI is transforming the world. OpenAI develops powerful models.",
    "Agents can automate workflows and handle complex reasoning tasks.",
    "Python is great for prototyping multi-agent systems."
]

# ==============================
# Agent 1：数据抓取
# ==============================
class DataFetcher:
    def __init__(self, data_source: List[str]):
        self.data_source = data_source

    def fetch(self):
        print("[数据抓取 Agent] 正在获取原始数据...")
        return self.data_source

# ==============================
# Agent 2：文本清洗
# ==============================
class TextCleaner:
    STOPWORDS = {"is", "the", "and", "for", "can"}

    def clean(self, texts: List[str]) -> List[str]:
        print("[文本清洗 Agent] 正在清洗文本...")
        cleaned = []
        for t in texts:
            t_lower = t.lower()
            t_no_punct = re.sub(r'[^\w\s]', '', t_lower)  # 去掉标点
            t_filtered = " ".join([w for w in t_no_punct.split() if w not in self.STOPWORDS])
            cleaned.append(t_filtered)
        return cleaned

# ==============================
# Agent 3：关键词提取（长链推理）
# ==============================
class KeywordExtractor:
    def extract(self, texts: List[str]) -> List[List[str]]:
        print("[关键词提取 Agent] 正在提取关键词（长链推理）...")
        keywords_list = []
        for t in texts:
            words = t.split()
            # 长链推理：根据词长度和字母顺序选择关键词
            keywords = sorted(words, key=lambda w: (-len(w), w))[:5]
            keywords_list.append(keywords)
        return keywords_list

# ==============================
# Agent 4：报告生成
# ==============================
class ReportGenerator:
    def generate(self, keywords_list: List[List[str]]):
        # 1️ 打印到终端（可读报告）
        for i, kws in enumerate(keywords_list, 1):
            print(f"文本 {i} 关键词：{', '.join(kws)}")

        # 2 写入 report.txt 文件（生成文件报告）
        with open("report.txt", "w", encoding="utf-8") as f:
            for i, kws in enumerate(keywords_list, 1):
                line = f"文本 {i} 关键词：{', '.join(kws)}\n"
                f.write(line)

# ==============================
# 多 Agent 流水线调度
# ==============================
class MultiAgentPipeline:
    def __init__(self):
        self.fetcher = DataFetcher(RAW_DATA)
        self.cleaner = TextCleaner()
        self.extractor = KeywordExtractor()
        self.reporter = ReportGenerator()

    def run(self):
        data = self.fetcher.fetch()
        clean_data = self.cleaner.clean(data)
        keywords = self.extractor.extract(clean_data)
        self.reporter.generate(keywords)

if __name__ == "__main__":
    pipeline = MultiAgentPipeline()
    pipeline.run()
