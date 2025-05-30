import csv
import random
import argparse
import traceback

def ask_llm(text):
    """
    Replace with actual model call
    """
    return "LLM response"  

def generate_multiple_choice(question, options, num):
    options += ' e)Something else' if num == 5 else ' k)Something else'
    instruction = " Choose from the options below: "
    return ask_llm(question + instruction + options)

def generate_false_answer(correct_answer):
    digit = len(answer)
    num = ''
    for i in range(digit):
        num = num + '9'

    end_num = int(num)

    random.seed(7)
    else_answer = random.sample(range(end_num), 1)
    if else_answer == int(answer):
        random.seed(9)
        else_answer = random.sample(range(end_num), 1)

    return float(else_answer[0])

def generate_random_selections(total_num, option_num):
    even_num = total_num // option_num  # Calculate the size of each interval

    total_num = total_num - even_num

    random_numbers = []

    for i in range(total_num):
      random_numbers.append(random.choice(range(option_num-1)))

    return random_numbers

def save_to_csv(filename, data):
    csv_columns = ['question', 'answer', 'options', 'gt_option', 'multi', 'saq', 'tf', 'yon']
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(data)
    except IOError:
        print("I/O error")

def generate_babi_wrong_answer(correct_answer, seed_num):
    options = ['kitchen', 'bedroom', 'garden', 'bathroom', 'hallway', 'office']
    options.remove(correct_answer)
    random.seed(seed_num)
    return random.choice(options, 1)

def main(dataset, output_file, num_options):
    results = []
    
    for i, entry in enumerate(dataset):
        print(f"Processing entry {i + 1}...")
        
        question = entry['question']
        answer = entry['answer']
        gt = entry['answer']
        options = entry['option']
        gt_option = entry['gt_option']
        
        # Generate multiple-choice options
        multiple_choice_response = generate_multiple_choice(question, options, num_options)
        
        # Generate short answer response
        saq_response = ask_llm(question)

        # Generate incorrect answer for GSM8K300 dataset (if applicable)
        answer = str(generate_false_answer(question, answer))
        
        # Generate incorrect answer for bAbI300 dataset (if applicable)
        answer = babi_wrong(answer, i)[0]

        # Generate True/False response
        """
        Need to pick one instruction!
        """
        # tf_instruction = " Is the answer " + answer + "?" + " Choose one of these. True or False"
        # tf_instruction = " Is the answer " + answer + "?" + " Solve the question first and choose. True or False"
        # tf_instruction = " The answer of the question is " + answer + "." + " True or False"
        # tf_instruction = " The answer of the question is " + answer + "." + " Solve the question first and choose. True or False"

        tf_response = ask_llm(question + tf_instruction)
                
        # Add result entry
        results.append({
            'question': question,
            'answer': gt,
            'options': options,
            'gt_option': gt_option,
            'multi': multiple_choice_response,
            'saq': saq_response,
            'tf': tf_response,
        })
    
    # Save results to CSV
    save_to_csv(output_file, results)

if __name__ == "__main__":
    parser.add_argument("input", type=str, help="You can use the given datasets")
    parser.add_argument("output", type=str, help="Output CSV file path")
    parser.add_argument("--num_options", type=int, choices=[5, 11], default=5, help="Number of multiple-choice options (5 or 11)")
    args = parser.parse_args()
    
    dataset = []  # Replace with an actual dataset
    
    try:
        main(dataset, args.output, args.num_options)
    except Exception as e:
        print("Error")
        traceback.print_exc()
