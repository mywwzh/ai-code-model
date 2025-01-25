import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

def predict_code(model_path, code_path):

    device = torch.device("cpu")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.to(device)
    model.eval()

    try:
        with open(code_path, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    try:
        inputs = tokenizer(code, 
                         truncation=True, 
                         padding=True, 
                         max_length=512, 
                         return_tensors="pt")
        
        with torch.no_grad():
            outputs = model(**inputs)
            probabilities = F.softmax(outputs.logits, dim=1)
            ai_probability = probabilities[0][1].item()
        
        return ai_probability

    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python run.py <code_file_path>")
        sys.exit(1)

    model_path = "./trained_ai_judge"
    code_path = sys.argv[1]
    
    prob = predict_code(model_path, code_path)
    if prob is not None:
        print(f"Probability of being AI generated code: {prob:.2%}")