from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device set to use {device}")

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def summarize(text):
    prompt = f"Summarize the following article:\n{text}\nSummary:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(device)
    outputs = model.generate(**inputs, max_new_tokens=150)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary.split("Summary:")[-1].strip()
