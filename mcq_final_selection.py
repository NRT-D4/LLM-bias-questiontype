import re
def extract_something(text):
    matches = re.findall(r'\b(something else|Something else|Something Else)\b', text, re.IGNORECASE)
    return matches

def clean_string(s):
        return s.replace(' ,', '').replace(', ', '').replace(',', '').replace(') $', ') ').replace('$', '').strip()


def clean_question(question):
    return re.sub(r'\s*[:,]\s*', '', question)

def final_accuracy_mcq(data, num_opt):

    count = 0

    for i, ele in enumerate(data):
        result = clean_string(ele['multi'])

        final_final = re.findall(r'([a-zA-Z]\))', result)

        if not final_final:
          if num_opt == 5:
                if ele['gt_option'] == 'e':
                  something = extract_something(result)
                  if something != []:
                    count += 1
                    data[i].update({'final': '1'})
                  else:
                    data[i].update({'final': '0'})
          else:
            if ele['gt_option'] == 'k':
              something = extract_something(result)
              if something != []:
                count += 1
                data[i].update({'final': '1'})
              else:
                data[i].update({'final': '0'})

        else:

          hmm = f"{ele['gt_option']})"

          if hmm in final_final:
              if hmm == final_final[-1]:
                count += 1
                data[i].update({'final': '1'})
              else:
                data[i].update({'final': '0'})
          else:
              if num_opt == 5:
                if ele['gt_option'] == 'e':
                  something = extract_something(result)
                  if something != []:
                    count += 1
                    data[i].update({'final': '1'})
                  else:
                    data[i].update({'final': '0'})
              else:
                if ele['gt_option'] == 'k':
                  something = extract_something(result)
                  if something != []:
                    count += 1
                    data[i].update({'final': '1'})
                  else:
                    data[i].update({'final': '0'})


    total_items = len(data)
    accuracy = count / total_items if total_items > 0 else 0

    print(f"Correct count: {count}")
    print(f"Total items: {total_items}")
    print(f"Accuracy: {accuracy:.2%}")

# example
"""
result: result csv file with output
num_options: 5 or 11
"""
final_accuracy_mcq(result, num_options)