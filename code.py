def count_element_frequencies(input_sequence):
    """
    Count the frequency of each element in the input sequence.
    
    Args:
    input_sequence (iterable): The input sequence (e.g., string or list) to analyze.
    
    Returns:
    dict: A dictionary where keys are unique elements from the input,
          and values are their frequencies.
    """
    frequency_dict = {}
    for element in input_sequence:
        if element not in frequency_dict:
            frequency_dict[element] = 1
        else:
            frequency_dict[element] += 1
    return frequency_dict


def print_relative_frequencies(frequency_dict):
    """
    Calculate and print the relative frequencies of elements in a frequency dictionary.
    
    Args:
    frequency_dict (dict): A dictionary where keys are elements and values are their frequencies.
    
    Prints:
    str: A header 'Relative Frequencies:' followed by each element and its relative frequency.
    """
    print('Relative Frequencies:')
    
    # Calculate the total count of all elements
    total_count = sum(frequency_dict.values())
    
    # Iterate through each element and its count in the dictionary
    for element, count in frequency_dict.items():
        # Calculate and print the relative frequency
        relative_frequency = count / total_count
        print(f"{element}: {relative_frequency:.4f}")


def analyze_dna_sequence(dna_sequence):
    """
    Analyze the frequency distribution of nucleotides in a DNA sequence.
    
    Args:
    dna_sequence (str): A string representing a DNA sequence.
    
    This function counts the frequency of each nucleotide in the input DNA sequence
    and then prints their relative frequencies.
    """
    # Count the frequencies of nucleotides
    nucleotide_frequencies = count_element_frequencies(dna_sequence)
    
    # Print the relative frequencies
    print_relative_frequencies(nucleotide_frequencies)


# Example usage
dna_sample = 'ATCTGACGCGCGCCGC'
print(f"Analyzing DNA sequence: {dna_sample}")
analyze_dna_sequence(dna_sample)