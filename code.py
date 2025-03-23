def get_other_dragons(dragon, dragons):
    """
    Returns a new list containing all dragons except the specified one
    
    Args:
        dragon: The dragon to exclude
        dragons: The list of all dragons
        
    Returns:
        list: A new list containing all dragons except the specified one
    """
    return [d for d in dragons if d != dragon]

def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]
    
    # Example usage
    green_dragon = dragons[0]
    other_dragons = get_other_dragons(green_dragon, dragons)
    # other_dragons will now contain Red, Blue and Black dragons
    