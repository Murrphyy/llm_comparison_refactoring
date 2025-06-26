import yaml
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from model.models import ModelType
import transformers
import gc
import os
 

class LLMHandler:
    def __init__(self, config_path: str):
        """
        Initializes the LLMHandler by reading the YAML config and loading the model.
        
        :param config_path: Path to the YAML configuration file.
        """
        self.config = self._load_config(config_path)
        self.model_name = self.config.get("model_name")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.tokenizer, self.model = self._load_model()
        

    def _load_config(self, config_path: str) -> dict:
        """Loads the YAML configuration file."""
        with open(config_path, "r") as file:
            return yaml.safe_load(file)

    def _load_model(self):
        """Loads the specified model and tokenizer from Hugging Face."""
        tokenizer = None
        model = None

        if self.model_name == ModelType.QWEN_15_LITE.value:
            model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype="auto",
                device_map="auto"
            )
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        elif self.model_name == ModelType.QWEN_25_LITE.value:
            model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype="auto",
                device_map="auto"
            )
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        elif self.model_name == ModelType.DEEPSEEK_LITE.value:
            tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
            model = AutoModelForCausalLM.from_pretrained(self.model_name, trust_remote_code=True, torch_dtype=torch.bfloat16).cuda()
        elif self.model_name == ModelType.LLAMA32_LITE.value:
            model = transformers.pipeline(
                "text-generation",
                model=self.model_name,
                model_kwargs={"torch_dtype": torch.bfloat16},
                device_map="auto",
            )
        elif self.model_name == ModelType.PHI_4_LITE.value:
            model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map="auto",
                torch_dtype="auto",
                trust_remote_code=True,
            )
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        else:            
            print("NO MODEL FOUND!\n")
        
        return tokenizer, model

    def generate_text(self, prompt: str) -> str:
        """
        Generates text using the loaded model.
        
        :param prompt: Input text for the model.
        :param max_length: Maximum length of the generated text.
        :return: Generated text.
        """
        if self.model_name == ModelType.QWEN_15_LITE.value:
            return self.generate_qwen_15_lite(prompt)
        elif self.model_name == ModelType.QWEN_25_LITE.value:
            return self.generate_qwen_25_lite(prompt)
        elif self.model_name == ModelType.DEEPSEEK_LITE.value:
            return self.generate_deepseek_lite(prompt)
        elif self.model_name == ModelType.LLAMA32_LITE.value:
            return self.generate_llama_32_lite(prompt)
        elif self.model_name == ModelType.PHI_4_LITE.value:
            return self.generate_phi_4_lite(prompt)
        print("NO MODEL FOUND!\n")
        return None

    def generate_phi_4_lite(self, prompt: str) -> str:
        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )
        
        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "do_sample": True,
        }
        
        output = pipe(prompt, **generation_args)
        response = output[0]['generated_text']
        
        return response

    def generate_llama_32_lite(self, prompt: str) -> str:
        outputs = self.model(
            prompt,
            max_new_tokens=256,
        )

        response = outputs[0]["generated_text"][-1]["content"]
        
        return response

    def generate_qwen_15_lite(self, prompt: str) -> str:
        text = self.tokenizer.apply_chat_template(
            prompt,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            model_inputs.input_ids,
            max_new_tokens=512
        )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        return response

    def generate_qwen_25_lite(self, prompt: str) -> str:
        text = self.tokenizer.apply_chat_template(
            prompt,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=512
        )

        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response

    def generate_deepseek_lite(self, prompt: str) -> str:
        inputs = self.tokenizer.apply_chat_template(prompt, add_generation_prompt=True, return_tensors="pt").to(self.model.device)
        attention_mask = inputs.ne(self.tokenizer.pad_token_id).to(self.model.device)
        # tokenizer.eos_token_id is the id of <｜end▁of▁sentence｜>  token
        outputs = self.model.generate(inputs, max_new_tokens=512, attention_mask = attention_mask, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1, eos_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)

        return response
