from transformers import LlamaForCausalLM, LlamaTokenizer

# Substitua pelo caminho ou ID do modelo ao qual você tem acesso
model_name = "meta-llama/Meta-Llama-3-8B"  # Por exemplo, "Meta/LLaMA-2-7B"

# Carregar o tokenizer e o modelo
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Função para gerar nomes de gatos
def generate_cat_names(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == '__main__':
    prompt = "Você tem um gatinho novo e gostaria de dar um nome legal para ele. Me dê uma lista de 5 possíveis nomes."
    nomes = generate_cat_names(prompt)
    print(nomes)

