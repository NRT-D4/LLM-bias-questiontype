Certainly! Here's your final `README.md` — with the **Acknowledgements** and **Repository Structure** sections removed, as requested:

---

# Is Large Language Model Performance on Reasoning Tasks Impacted by Different Ways Questions Are Asked?

📄 \[**Paper**] | \[**arXiv**]

Official repo for the ACL 2025 Findings paper:
**Is Large Language Model Performance on Reasoning Tasks Impacted by Different Ways Questions Are Asked?**
**Seok Hwan Song, Mohna Chakraborty, Qi Li, Wallapak Tavanapong**

📌 *Accepted to Findings of ACL 2025*

We introduce the **first benchmark framework** to examine how the *format of a question*—Short Answer (SAQ), Multiple Choice (MCQ), or True/False (TFQ)—affects **LLM performance on reasoning tasks**.
Our findings reveal that **question types significantly alter both reasoning and final answer accuracy**, even for the exact same underlying problem.

---

## 🧪 Experiments

### Required Libraries

This repository uses standard Python libraries:

```
re, csv, random, argparse, traceback
```

---

### Running the Inference

The script `execution.py` handles LLM interaction for all question types.

#### To run it:

```bash
python execution.py
```

You will need to:

1. **Select and implement your LLM** inside the script.
2. **Choose an instruction format** (only for TFQ).
3. **Select a dataset** to load (`gsm8k300` or `babi300`).

Example (inside `execution.py`):

* Model: `gpt-4o`
* Dataset: `gsm8k300/`
* Question Type: `tfq`
* Instruction: `"Solve the question first and choose True or False"`

Outputs will be saved to the `results/` folder (you may need to create it manually).

---

### Evaluating Final Selection Accuracy

After generating predictions, use the following scripts to calculate final answer correctness:

* For **Multiple Choice Questions (MCQ)**:

```bash
python mcq_final_selection.py
```

* For **True/False Questions (TFQ)**:

```bash
python tfq_final_selection.py
```

Both scripts require you to provide the result file paths and compare them to the expected labels.

> 💡 *Note: Reasoning accuracy must be manually reviewed, as it cannot be automatically assessed.*

---

## 📎 Citation

If you use this work, please cite:

```bibtex
@inproceedings{
  song2025questiontypes,
  title={Is Large Language Model Performance on Reasoning Tasks Impacted by Different Ways Questions Are Asked?},
  author={Song, Seok Hwan and Chakraborty, Mohna and Li, Qi and Tavanapong, Wallapak},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},
  year={2025}
}
```

---

Let me know if you'd like this exported into a markdown file or uploaded to your GitHub.
