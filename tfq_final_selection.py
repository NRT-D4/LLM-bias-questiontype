import re

def extract_true_false(text):
    matches = re.findall(r'\b(true|True|TRUE|FALSE|False|false)\b', text, re.IGNORECASE)
    return matches

def clean_question(question):
    return re.sub(r'\s*[:,]\s*', '', question)

def final_accuracy_tof(data, tof):

    def clean_string(s):
        return s.replace(' ,', '').replace(', ', '').replace(',', '').replace(') $', ') ').replace('$', '').strip()

    count = 0

    for i, ele in enumerate(data):
        result = ele['tf']

        true_false = extract_true_false(result)

        if true_false != []:
            if tof:
                if true_false[-1] == 'true' or true_false[-1] == 'True' or true_false[-1] == 'TRUE':
                    count += 1
                    data[i].update({'final': '1'})
                else:
                    data[i].update({'final': '0'})
            else:
                if true_false[-1] == 'false' or true_false[-1] == 'False' or true_false[-1] == 'FALSE':
                    count += 1
                    data[i].update({'final': '1'})
                else:
                    data[i].update({'final': '0'})
        else:
            data[i].update({'final': '0'})


    total_items = len(data)
    accuracy = count / total_items if total_items > 0 else 0

    print(f"Correct count: {count}")
    print(f"Total items: {total_items}")
    print(f"Accuracy: {accuracy:.2%}")


# Example
"""
result: result csv file
tof: True --> "True" as a correct answer
     False --> "False" as a correct answer
"""
final_accuracy_tof(result_file, tof)