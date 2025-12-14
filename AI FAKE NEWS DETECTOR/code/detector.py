from keywords import fake_keywords, real_keywords

def detect_fake_news(headline):
    """Analyze a news headline to determine its authenticity.
    
    Args:
        headline (str): The news headline to analyze
        
    Returns:
        tuple: (result_category, confidence_percentage)
               where result_category is "Fake News", "Real News", or "Unclear"
               and confidence_percentage is 0-100
    """
    
    # Normalize the input to lowercase for case-insensitive matching
    headline = headline.lower()
    
    # Calculate fake score by summing weights of all matched fake keywords
    fake_score = sum(
        weight 
        for word, weight in fake_keywords.items() 
        if word in headline  # Check for keyword presence
    )
    
    # Calculate real score by summing weights of all matched real keywords
    real_score = sum(
        weight 
        for word, weight in real_keywords.items() 
        if word in headline  # Check for keyword presence
    )

    # Determine total weight of all matched keywords
    total_score = fake_score + real_score
    
    # Calculate confidence percentage (0-100):
    # - Ratio of dominant score to total score
    # - 0% if no keywords matched (total_score == 0)
    confidence = (
        0 if total_score == 0 
        else (max(fake_score, real_score) / total_score) * 100
    )

    # Determine result category based on score comparison
    if fake_score > real_score:
        return "Fake News", confidence  # Fake keywords dominated
    elif real_score > fake_score:
        return "Real News", confidence  # Real keywords dominated
    else:
        return "Unclear", 50  # Equal scores or no keywords found