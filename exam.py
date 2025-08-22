from collections import Counter
import statistics

def main():
    """Main function to run all interview question solutions"""
    
    # Color data from the HTML table////
    colors_data = {
        'MONDAY': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
        'TUESDAY': ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
        'WEDNESDAY': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
        'THURSDAY': ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
        'FRIDAY': ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
    }
    
    # QUESTION 1: Which color of shirt is the mean color?
    print("\n1. MEAN COLOR ANALYSIS:")
    print("-" * 30)
    mean_color = find_mean_color(colors_data)
    print(f"The mean color is: {mean_color}")
    
    # QUESTION 2: Which color is mostly worn throughout the week?
    print("\n2. MOST WORN COLOR:")
    print("-" * 30)
    most_worn = find_most_worn_color(colors_data)
    print(f"Most worn color: {most_worn[0]} (worn {most_worn[1]} times)")
    
    # QUESTION 3: Which color is the median?
    print("\n3. MEDIAN COLOR:")
    print("-" * 30)
    median_color = find_median_color(colors_data)
    print(f"The median color is: {median_color}")
    
    # QUESTION 4: Get the variance of the colors
    print("\n4. COLOR VARIANCE:")
    print("-" * 30)
    variance = calculate_color_variance(colors_data)
    print(f"Variance of colors: {variance:.4f}")
    
    # QUESTION 5: What is the probability of choosing red on Friday?
    print("\n5. PROBABILITY OF RED ON FRIDAY:")
    print("-" * 30)
    red_probability = probability_red_friday(colors_data)
    print(f"Probability of choosing RED on Friday: {red_probability:.4f} or {red_probability*100:.2f}%")
    
    # Additional Analysis
    print("\n6. ADDITIONAL ANALYSIS:")
    print("-" * 30)
    additional_analysis(colors_data)
    
    # BINARY PATTERN PROBLEM
    print("\n7. BINARY PATTERN SOLUTION:")
    print("-" * 30)
    binary_pattern_solution()

def find_mean_color(colors_data):
    """Find the mean color (most frequent color representing the average)"""
    all_colors = []
    for day_colors in colors_data.values():
        all_colors.extend(day_colors)
    
    # Count frequencies
    color_counts = Counter(all_colors)
    
    # The mean color is the most frequent (mode as approximation of mean)
    mean_color = color_counts.most_common(1)[0][0]
    
    return mean_color

def find_most_worn_color(colors_data):
    """Find the color worn most throughout the week"""
    all_colors = []
    for day_colors in colors_data.values():
        all_colors.extend(day_colors)
    
    color_counts = Counter(all_colors)
    most_common = color_counts.most_common(1)[0]
    
    return most_common

def find_median_color(colors_data):
    """Find the median color"""
    all_colors = []
    for day_colors in colors_data.values():
        all_colors.extend(day_colors)
    
    # Sort colors alphabetically
    sorted_colors = sorted(all_colors)
    
    # Find median position
    n = len(sorted_colors)
    median_index = n // 2
    
    if n % 2 == 0:
        # Even number of colors, take the middle-right one
        median_color = sorted_colors[median_index]
    else:
        # Odd number of colors
        median_color = sorted_colors[median_index]
    
    return median_color

def calculate_color_variance(colors_data):
    """Calculate variance of color frequencies"""
    all_colors = []
    for day_colors in colors_data.values():
        all_colors.extend(day_colors)
    
    # Get color counts
    color_counts = Counter(all_colors)
    frequencies = list(color_counts.values())
    
    # Calculate variance
    variance = statistics.variance(frequencies)
    
    return variance

def probability_red_friday(colors_data):
    """Calculate probability of choosing RED on Friday"""
    friday_colors = colors_data['FRIDAY']
    
    red_count = friday_colors.count('RED')
    total_count = len(friday_colors)
    
    probability = red_count / total_count
    
    return probability

def additional_analysis(colors_data):
    """Provide additional insights"""
    all_colors = []
    for day_colors in colors_data.values():
        all_colors.extend(day_colors)
    
    color_counts = Counter(all_colors)
    
    print(f"Total colors recorded: {len(all_colors)}")
    print(f"Unique colors: {len(color_counts)}")
    print("\nColor frequency distribution:")
    for color, count in color_counts.most_common():
        percentage = (count / len(all_colors)) * 100
        print(f"  {color}: {count} times ({percentage:.1f}%)")
    
    # Daily analysis
    print("\nDaily color counts:")
    for day, colors in colors_data.items():
        print(f"  {day}: {len(colors)} colors")

def binary_pattern_solution():
    """Solve the binary pattern problem"""
    input_sequence = "0101101011101011011101101000111"
    
    print(f"Input:  {input_sequence}")
    
    #wherever "111" appears, output "1", otherwise "0"
    output = []
    
    i = 0
    while i < len(input_sequence):
        # Check if current position starts with "111"
        if i <= len(input_sequence) - 3 and input_sequence[i:i+3] == "111":
            output.append('1')
            i += 3  # Skip the next 2 characters since we processed "111"
        else:
            output.append('0')
            i += 1
    
    output_sequence = ''.join(output)
    expected_output = "0000000000100000000100000000001"
    
    print(f"Output: {output_sequence}")
    print(f"Expected: {expected_output}")
    print(f"Match: {'YES' if output_sequence == expected_output else 'NO'}")
    
    alt_output = ['0'] * len(input_sequence)
    for i in range(len(input_sequence) - 2):
        if input_sequence[i:i+3] == "111":
            alt_output[i] = '1'
    
    alt_output_sequence = ''.join(alt_output)
    print(f"Alternative: {alt_output_sequence}")
    print(f"Alt Match: {'YES' if alt_output_sequence == expected_output else 'NO'}")

if __name__ == "__main__":
    main()