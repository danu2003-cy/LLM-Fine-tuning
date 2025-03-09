
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "/content/saved_model"

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", offload_folder="/content/offload")
tokenizer = AutoTokenizer.from_pretrained(model_name)

text_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

def generate_text(prompt, max_length=50, max_new_tokens=50):
    result = text_pipeline(prompt, max_length=max_length, max_new_tokens=max_new_tokens, truncation=True)
    return result[0]['generated_text']
