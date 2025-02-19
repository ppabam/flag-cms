def is_similar(input_text, correct_text, match_threshold=5):
    input_text = input_text.replace(" ", "")
    correct_text = correct_text.replace(" ", "")

    match_count = 0
    for a, b in zip(input_text, correct_text):
        if a == b:
            match_count += 1
        
    return match_count >= match_threshold