def hanoi_solver(disks: int) -> str:
    # Recursive Approach with Higher Order Functions

    # Initialize the three Hanoi Towers and a List of Moves
    towers  = {
        'First': [n for n in range(disks, 0, -1)],
        'Mid': [],
        'Last': []
    }
    move_list = [f'{towers["First"]} {towers["Mid"]} {towers["Last"]}']

    
    def move_disk(n, source, reserve, destination):
        if n == 0:
            return
        
        move_disk(n - 1, source, destination, reserve)

        # Single-Line Stack Transfer Operation: Append the Removed item from Source to Destination
        towers[destination].append(towers[source].pop())
        move_list.append(f'{towers["First"]} {towers["Mid"]} {towers["Last"]}')

        move_disk(n - 1, reserve, source, destination)

    move_disk(disks, 'First','Mid', 'Last')

    return '\n'.join(move_list)



