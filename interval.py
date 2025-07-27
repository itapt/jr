import random

def generate_inverval(candidates_count: int) -> list[int]:
    """
    Returns a contiguous subset of candidates' list [0, ..., candidates_count -1]
    """
    random_pos = random.randint(0, candidates_count - 1)
    random_offset = random.randint(0, candidates_count - random_pos)

    return [x for x in range(random_pos, random_pos + random_offset)]
