import json
from textstat import textstat


def classify_text_level(text):
    # Classificação simplificada baseada no índice de legibilidade Flesch-Kincaid
    flesch_kincaid = textstat.flesch_kincaid_grade(text)

    if flesch_kincaid <= 2:
        return "A1"
    elif flesch_kincaid <= 4:
        return "A2"
    elif flesch_kincaid <= 6:
        return "B1"
    elif flesch_kincaid <= 8:
        return "B2"
    elif flesch_kincaid <= 10:
        return "C1"
    else:
        return "C2"


def process_large_json(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        text = item.get('text', '')
        item['level'] = classify_text_level(text)

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Classificação completa. Saída salva em {output_path}")


# Especifica os caminhos para seus arquivos de entrada e saída
input_file = 'TextCollection.json'
output_file = 'TextCollection_classified.json'

# Processa o grande arquivo JSON
process_large_json(input_file, output_file)
