import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction, molecular_weight
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DNAAnalyze:
    def __init__(self, root):
        self.root = root
        self.root.title("Genome Sequence Analyzer")
        self.root.configure(bg='#ADD8E6')

       
        # Bind window resize event
        self.root.bind("<Configure>", self.on_resize)

        # Custom style for larger font
        self.root.style = ttk.Style()
        self.root.style.configure('LargeFont.TButton', font=('Helvetica', 16))
        self.root.style.configure('LargeFont.TLabel', font=('Helvetica', 16))
        self.root.style.configure('LargeFont.TCheckbutton', font=('Helvetica', 16))
        self.root.style.configure('LargeFont.TEntry', font=('Helvetica', 16))

        self.input_frame = ttk.LabelFrame(root, text="Infuse Nucleotide Sequence")
        self.input_frame.pack(pady=50)

        self.dna_label = ttk.Label(self.input_frame, text="Nucleotide Sequence:",style='LargeFont.TLabel')
        self.dna_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.dna_entry = ttk.Entry(self.input_frame, width=30)
        self.dna_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.open_file_button = ttk.Button(self.input_frame, text="Open File", command=self.open_file, style='LargeFont.TButton')
        self.open_file_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.checkbox_frame = ttk.LabelFrame(root, text="Select Operations to Perform")
        self.checkbox_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.checkbox_vars = {
            "Length": tk.BooleanVar(),
            "Reverse Complement": tk.BooleanVar(),
            "Transcription": tk.BooleanVar(),
            "Translation": tk.BooleanVar(),
            "GC Content": tk.BooleanVar(),
            "Molecular Weight": tk.BooleanVar(),
            "AT Content": tk.BooleanVar(),
            "Count Nucleotides": tk.BooleanVar(),
            "Palindrome Check": tk.BooleanVar(),
            "Visualize Sequence": tk.BooleanVar(),
            # Add more functions here as needed
        }

        self.create_checkboxes()

        self.analyze_button = ttk.Button(root, text="Analyze", command=self.analyze_sequence, style='LargeFont.TButton')
        self.analyze_button.pack(pady=20)

    def create_checkboxes(self):
        # Calculate the number of rows needed based on the number of checkboxes
        num_rows = (len(self.checkbox_vars) + 1) // 2

        for i, (label, var) in enumerate(self.checkbox_vars.items()):
            row, column = divmod(i, 2)
            checkbox = ttk.Checkbutton(
                self.checkbox_frame, text=label, variable=var,
                style='LargeFont.TCheckbutton', command=lambda: self.update_checkbox_state(checkbox)
            )
            checkbox.grid(row=row, column=column, padx=150, pady=15, sticky="w")

    def on_resize(self, event):
        # Update geometry on window resize
        self.root.update_idletasks()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.dna_entry.delete(0, tk.END)
                self.dna_entry.insert(0, file.read())

    def analyze_sequence(self):
        dna_sequence = self.dna_entry.get().upper()

        if not dna_sequence:
            messagebox.showwarning("Warning", "Please enter a DNA sequence.")
            return

        results = []
        for label, var in self.checkbox_vars.items():
            if var.get():
                result = self.perform_operation(label, dna_sequence)
                results.append(f"{label}: {result}")

        result_text = "\n".join(results)

        result_window = tk.Toplevel(self.root)
        result_window.title("Analysis Results")

        results_text_widget = scrolledtext.ScrolledText(result_window, wrap="word", height=15, width=70, font=('Helvetica', 16))
        results_text_widget.insert(tk.END, result_text)
        results_text_widget.pack(pady=20, fill=tk.BOTH, expand=True)

    def update_checkbox_state(self, checkbox):
        # Ensure checkbox stays selected when clicked
        checkbox.state(['!alternate'])

    def perform_operation(self, operation, dna_sequence):
        sequence = Seq(dna_sequence)

        if operation == "Length":
            return len(sequence)
        elif operation == "Reverse Complement":
            return sequence.reverse_complement()
        elif operation == "Transcription":
            return sequence.transcribe()
        elif operation == "Translation":
            return sequence.translate()
        elif operation == "GC Content":
            return f"{gc_fraction(sequence) * 100:.2f}%"
        elif operation == "Molecular Weight":
            try:
                return f"{molecular_weight(sequence):.2f}"
            except ValueError as e:
                return str(e)
        elif operation == "AT Content":
            return f"{(sequence.count('A') + sequence.count('T')) / len(sequence) * 100:.2f}%"
      
        elif operation == "Count Nucleotides":
            return f"A: {sequence.count('A')}, T: {sequence.count('T')}, C: {sequence.count('C')}, G: {sequence.count('G')}"
      
        elif operation == "Palindrome Check":
            return sequence == sequence.reverse_complement()
        elif operation == "Visualize Sequence":
            self.visualize_sequence(sequence)
            return "Visualization Displayed"
        # Add more functions here as needed

    def visualize_sequence(self, sequence):
        nucleotides = ['A', 'T', 'C', 'G']
        frequencies = [sequence.count(base) for base in nucleotides]

        fig, ax = plt.subplots()
        ax.bar(nucleotides, frequencies)
        ax.set_title("Nucleotide Frequencies")
        ax.set_xlabel("Nucleotide")
        ax.set_ylabel("Frequency")

        result_window = tk.Toplevel(self.root)
        result_window.title("Visualization")

        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = DNAAnalyze(root)
    root.mainloop()
