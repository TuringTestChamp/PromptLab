
import random

class AIIntegration:
    def __init__(self):
        pass

    def enhance_prompt(self, original_prompt):
        words = original_prompt.split(', ')
        random.shuffle(words)  # Shuffle the words for variation
        
        # Create two distinct variations
        # Variation 1: Remove a random word/phrase
        gen_prompt_1 = ', '.join(words[:-1]) if len(words) > 1 else original_prompt
        
        # Variation 2: Swap positions of two random words/phrases
        if len(words) > 2:
            idx1, idx2 = random.sample(range(len(words)), 2)
            words[idx1], words[idx2] = words[idx2], words[idx1]
            gen_prompt_2 = ', '.join(words)
        else:
            gen_prompt_2 = original_prompt
        
        return gen_prompt_1, gen_prompt_2

    # Future methods for real AI integration can be added here, e.g., calling OpenAI API
