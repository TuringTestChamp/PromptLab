
import random

class AIIntegration:
    def __init__(self):
        pass

    def enhance_prompt(self, original_prompt):
        # Mock AI function for demonstration purposes
        words = original_prompt.split(', ')
        random.shuffle(words)  # Shuffle the words for variation
        
        # Add "enhanced" or "refined" to a random position
        gen_prompt_1 = ', '.join(words[:2] + ["enhanced"] + words[2:])
        gen_prompt_2 = ', '.join(words[:3] + ["refined"] + words[3:])
        
        return gen_prompt_1, gen_prompt_2

    # Future methods for real AI integration can be added here, e.g., calling OpenAI API
