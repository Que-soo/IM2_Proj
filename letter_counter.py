
def char_frequency(text):
    freq = {}
    for ch in text:
        if ch != " ":  
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def main():
    
    user = input("Enter string: ")
    
    result = char_frequency(user)

    output = []
    for key, value in result.items():
        output.append(f"{key}={value}")
    print(", ".join(output))

if __name__ == "__main__":
    main()