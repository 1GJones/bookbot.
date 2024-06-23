
def count_words(text):
    words = text.split()
    return len(words)

def character_frequency(text):
    frequency={}
    for char in text.lower():
        if char.isalpha in frequency :
            frequency[char]+=1
           
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    return frequency

    
def create_report(word_count, char_freq):
    report = []
    report.append(f"Number of words in the book: {word_count}")
    report.append("Character frequency:")
    
    for char, freq in sorted(char_freq.items()):
        report.append(f"{char}: {freq}")
    
    return "\n".join(report)    
def main():
    with open("books/frankenstein.txt", "r") as f:
     content = f.read()
     char_freq = character_frequency(content)
     word_count = count_words(content)
      
    report=create_report(word_count, char_freq)
    print(f"Number of word in the book: {count_words(content),}")
    print(character_frequency(content))
    print(report)
  
  
  
  
  
  
  
if __name__ == "__main__":
    main()
 