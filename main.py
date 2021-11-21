def check_sequence(seq):
    open_seq = {'(': ')', '[': ']', '{': '}'}
    close_seq = {')': '(', ']': '[', '}': '{'}
    if seq == '':
        return True
    if len(seq) % 2 == 1:
        return False
    if seq[0] in close_seq:
        return False
    stack = []
    for i in seq:
        if i in open_seq:
            stack.append(i)
        elif i in close_seq and len(stack) == 0:
            return False
        elif i in close_seq and close_seq[i] != stack[-1]:
            return False
        else:
            stack.pop(-1)
    return len(stack) == 0


sequence = input()
print("YES" if check_sequence(sequence) else "NO")
