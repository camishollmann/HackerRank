# Problem statement:
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# NOT SOLVED (YET).

if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append((name, score))
                
        lowest_grade = min(records[i])
        print(lowest_grade)


    # CHATGPT SOLUTION: 
    if __name__ == '__main__':
    records = []  # Store (name, score) pairs

    # Read input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name, score))  # Store as tuple (name, score)

    # Extract only the scores
    scores = [score for _, score in records]  

    # Find the minimum score
    lowest_grade = min(scores)

    # Find all names with the lowest score
    lowest_names = [name for name, score in records if score == lowest_grade]

    # Print results
    print("Lowest Grade:", lowest_grade)
    print("Names with Lowest Grade:", lowest_names)
