
import tkinter as tk
from database_handling import FinalDatabase
from gui_handling import FinalAiRefinementGui

class FinalApp:
    def __init__(self, root):
        self.root = root
        self.database = FinalDatabase("refinement.db")
        self.gui = FinalAiRefinementGui(root, self.database)

    def run(self):
        self.root.mainloop()

# To run the application on your local machine:
if __name__ == "__main__":
    root = tk.Tk()
    app = FinalApp(root)
    app.run()
