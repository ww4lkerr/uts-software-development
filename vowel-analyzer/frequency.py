from pathlib import Path

text = Path("data.txt").read_text(encoding="utf-8").lower()

vowels = "aeiou"
counts = {vowel: text.count(vowel) for vowel in vowels}

print("Vowel Frequency Results")
for vowel, count in counts.items():
    print(f"{vowel}: {count}")