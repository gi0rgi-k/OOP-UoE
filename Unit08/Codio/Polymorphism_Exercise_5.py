source_file = '/home/codio/workspace/code/polymorphism/text_1_exercise5.txt'
answer_file = '/home/codio/workspace/code/polymorphism/answer_exercise5.txt'

class Substitute:
    def __init__(self, source_file, answer_file):
        """
        Initialize the Substitute class with source and answer file paths.

        :param source_file: str, path to the source file to read
        :param answer_file: str, path to the answer file to write
        """
        self.source_file = source_file
        self.answer_file = answer_file
        self.words = None
    
    def string_to_list(self):
        """
        Read text file, turn it into a 2D list of words for each line.
        """
        words = []
        with open(self.source_file, 'r') as file_object:
            lines = file_object.read().split('\n')
            for line in lines:
                words.append(line.split())
        self.words = words
    
    def list_to_string(self):
        """
        Convert 2D list back into a string with newline characters.
        """
        lines = []
        for line in self.words:
            lines.append(' '.join(line))
        self.words = '\n'.join(lines)  # Ensure this creates a single string with newlines
  
    def swap_words(self):
        """
        Replace every fifth word with 'HELLO'.
        """
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 5 == 0:
                    word = line[i]
                    line[i] = 'HELLO'
        self.list_to_string()

class Stars(Substitute):
    def swap_words(self):
        """
        Override the swap_words method to replace every third word with a series of *.
        The number of * should match the number of characters in the word.
        """
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 3 == 0:
                    word = line[i]
                    line[i] = '*' * len(word)
        self.list_to_string()
        # Write the new string to the answer file
        with open(self.answer_file, 'w') as file_object:
            file_object.write(self.words)

# Testing the Stars class
stars = Stars(source_file, answer_file)
stars.swap_words()

# Checking the output
with open(answer_file, 'r') as file_object:
    print(file_object.read())
