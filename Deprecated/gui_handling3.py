
import tkinter as tk
from tkinter import messagebox
from database_handling import FinalDatabase
from ai_integration import AIIntegration

class FinalAiRefinementGui:
    def __init__(self, root, database):
        self.root = root
        self.root.title("AI Refinement GUI")
        self.database = database
        self.iteration_count = 0
        self.ai = AIIntegration()
        
        # GUI elements
        self.prompt_entry_label = tk.Label(self.root, text="Enter Original Prompt:")
        self.prompt_entry_label.pack(pady=10)
        
        self.prompt_entry = tk.Entry(self.root, width=100)
        self.prompt_entry.pack(pady=10)
        
        self.generate_button = tk.Button(self.root, text="Generate Enhanced Prompts", command=self.add_prompt)
        self.generate_button.pack(pady=20)
        
        self.prompt_display_1 = tk.Label(self.root, text="", wraplength=600)
        self.prompt_display_1.pack(pady=10)
        self.copy_prompt_button_1 = tk.Button(self.root, text="Copy Prompt 1", command=lambda: self.copy_to_clipboard(self.prompt_display_1.cget("text")))
        self.copy_prompt_button_1.pack(pady=5)
        
        self.prompt_display_2 = tk.Label(self.root, text="", wraplength=600)
        self.prompt_display_2.pack(pady=10)
        self.copy_prompt_button_2 = tk.Button(self.root, text="Copy Prompt 2", command=lambda: self.copy_to_clipboard(self.prompt_display_2.cget("text")))
        self.copy_prompt_button_2.pack(pady=5)
        
        self.select_prompt_button_1 = tk.Button(self.root, text="Select Prompt 1", command=self.select_prompt_1)
        self.select_prompt_button_1.pack(pady=10)
        
        self.select_prompt_button_2 = tk.Button(self.root, text="Select Prompt 2", command=self.select_prompt_2)
        self.select_prompt_button_2.pack(pady=10)

        self.dislike_both_button = tk.Button(self.root, text="Dislike Both Prompts", command=self.dislike_both)
        self.dislike_both_button.pack(pady=20)
        
    def add_prompt(self):
        self.original_prompt = self.prompt_entry.get() if self.iteration_count == 0 else self.selected_prompt
        gen_prompt_1, gen_prompt_2 = self.ai.enhance_prompt(self.original_prompt)
        
        # Display the generated prompts
        self.prompt_display_1.config(text=gen_prompt_1)
        self.prompt_display_2.config(text=gen_prompt_2)
        
    def select_prompt_1(self):
        self.selected_prompt = self.prompt_display_1.cget("text")
        self.store_feedback_and_proceed("Preferred")
        
    def select_prompt_2(self):
        self.selected_prompt = self.prompt_display_2.cget("text")
        self.store_feedback_and_proceed("Preferred")

    def dislike_both(self):
        self.database.store_feedback(self.iteration_count, "Disliked Both", "")
        self.iteration_count += 1
        self.add_prompt()
        
    def store_feedback_and_proceed(self, feedback_type):
        added, removed, retained = self.analyze_changes(self.original_prompt, self.selected_prompt)
        self.database.store_detailed_feedback(self.iteration_count, feedback_type, self.selected_prompt, added, removed, retained)
        self.iteration_count += 1
        self.add_prompt()
        
    def analyze_changes(self, original, enhanced):
        original_set = set(original.split(', '))
        enhanced_set = set(enhanced.split(', '))
        
        added = ', '.join(list(enhanced_set - original_set))
        removed = ', '.join(list(original_set - enhanced_set))
        retained = ', '.join(list(original_set & enhanced_set))
        
        return added, removed, retained

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()  # This is necessary to finalize the clipboard update
        messagebox.showinfo("Info", "Prompt copied to clipboard!")

