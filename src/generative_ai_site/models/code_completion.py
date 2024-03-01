from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Define the function for code completion
def get_code_completion(input_code):
    # Define the checkpoint for the smaller model and ensure it's available
    checkpoint = "Salesforce/codegen-350M-mono"
    
    # Load the model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    
    # Ensure the model uses the appropriate device (GPU if available, else CPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    # Prepare the input text for the model
    inputs = tokenizer.encode(input_code, return_tensors="pt").to(device)
    
    # Generate the completion using the model
    completion = model.generate(inputs, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    
    # Decode and return the generated text
    completed_code = tokenizer.decode(completion[0], skip_special_tokens=True)
    
    return completed_code

