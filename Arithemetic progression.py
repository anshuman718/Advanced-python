

def calculate_ap():
    a1 = 0
    an = 500
    n = 50
    
    # an = a1 + (n - 1) * d
    # 500 = 0 + 49 * d
    d = (an - a1) / (n - 1)
    
    # Elements are a1, a2, ..., an
    # The intervals would be between elements, or does "second and last second interval" mean the elements themselves or the intervals?
    # Usually, "second interval" means the second term, or the interval between 2nd and 3rd? Let's write out the terms.
    terms = [a1 + i * d for i in range(n)]
    return d, terms

d, terms = calculate_ap()
print(f"Common difference d: {d}")
print(f"First few terms: {terms[:5]}")
print(f"Last few terms: {terms[-5:]}")
