def find_two_sneaky_numbers(nums: list[int]) -> list[int]:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    result = []

    for num, frequency in counts.items():
        if frequency == 2:
            result.append(num)
            
        if len(result) == 2:
            break
            
    return result

test_nums = [1, 3, 4, 1, 3, 2, 0]
print(f"The sneaky numbers are: {find_two_sneaky_numbers(test_nums)}")
