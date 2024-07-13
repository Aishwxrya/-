
---

# Genome Sequence Analysis Tool

This project is a Python-based tool for performing various analyses on DNA and RNA sequences. It provides functionalities to calculate transcriptions, translations, nucleotide content, palindrome checks, and sequence lengths.

## Features

- **Transcription:** Convert DNA sequences to RNA sequences.
- **Translation:** Convert RNA sequences to protein sequences using standard genetic code.
- **Nucleotide Content:**
  - Calculate Adenine (A) and Thymine (T) content.
  - Calculate Cytosine (C) and Guanine (G) content.
- **Counting Nucleotides:** Count occurrences of each nucleotide (A, T, C, G).
- **Palindrome Checks:** Identify palindromic sequences within the DNA or RNA.
- **Sequence Length:** Calculate the length of DNA or RNA sequences.

## Requirements

- Python 3.x
- Libraries:
  - `numpy` for numerical operations (e.g., nucleotide counting)
  - `biopython` for sequence manipulation (e.g., transcription, translation)
  - Other dependencies as outlined in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/genome-sequence-analysis.git
   cd genome-sequence-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python main.py
   ```

## Usage

To use the tool, import the necessary functions/classes into your Python script:

```python
from genome_analysis import transcription, translation, nucleotide_count, palindrome_check, calculate_at_content, calculate_cg_content, calculate_sequence_length
```

Example usage:

```python
dna_sequence = "ATCGATCGATCG"
rna_sequence = transcription(dna_sequence)
protein_sequence = translation(rna_sequence)

a_count = calculate_nucleotide_count(dna_sequence, 'A')
t_count = calculate_nucleotide_count(dna_sequence, 'T')
c_count = calculate_nucleotide_count(dna_sequence, 'C')
g_count = calculate_nucleotide_count(dna_sequence, 'G')

at_content = calculate_at_content(dna_sequence)
cg_content = calculate_cg_content(dna_sequence)

is_palindromic = palindrome_check(dna_sequence)

dna_length = calculate_sequence_length(dna_sequence)
rna_length = calculate_sequence_length(rna_sequence)
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This tool uses the Biopython library for sequence manipulations.

---
