import time 
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class.",
    "Python programming is fun and rewarding.",
    "Typing speed tests can help improve your typing skills.",
    "Practice makes perfect when it comes to typing fast and accurately.",
    "The rain in Spain stays mainly in the plain.",
    "She sells seashells by the seashore.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "Abdul kalam was a great scientist and former president of India."
    
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy

def typing_test():
    # Select a random sentence for the test
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter when you are ready...")
    start_time = time.time()
    user_input = input("\nStart typing:\n")
    end_time = time.time()
    time_taken = end_time - start_time 
    word_count = len(test_sentence.split(" "))

    print("Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / (time_taken / 60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()

