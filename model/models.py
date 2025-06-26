from enum import Enum

class ModelType(Enum):
    """Enumeration of different model types."""
    
    QWEN_15_LITE = "Qwen/CodeQwen1.5-7B-Chat" 
    QWEN_25_LITE = "Qwen/Qwen2.5-Coder-7B-Instruct" 
    DEEPSEEK_LITE = "deepseek-ai/deepseek-coder-6.7b-instruct" 
    LLAMA32_LITE = "meta-llama/Llama-3.2-3B-Instruct" 
    PHI_4_LITE = "microsoft/Phi-4-mini-instruct" 