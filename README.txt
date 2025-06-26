# Comparison of LLMs for Automated Code Refactoring

This project compares various Large Language Models (LLMs) for the task of automated code refactoring. The framework allows you to test and evaluate multiple models on real-world Python code samples.

---

## 🚀 Features

- Supports 5 popular LLMs for code refactoring
- Works on sample Python files in batch
- Flexible model configuration via `model.yaml`
- Designed for experimentation and evaluation in research or production
- Uses CodeNet dataset


Specify one of the following in `CodeBase/model.yaml`:

- `Qwen/CodeQwen1.5-7B-Chat`
- `deepseek-ai/deepseek-coder-6.7b-instruct`
- `meta-llama/Llama-3.2-3B-Instruct`
- `Qwen/Qwen2.5-Coder-7B-Instruct`
- `microsoft/Phi-4-mini-instruct`

Specify one of the following in `CodeBase/prompts.yaml`:

- `few_shot`
- `zero_shot`
- `rci`

Dependencies:

- pip install -r requirements.txt

Data:

- data/Python_wrapped 
- data/Problem_descriptions 
- selected_files.txt

Run :

- inference.main