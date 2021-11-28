def is_braces_sequence_correct(seq: str) -> bool:
    open_seq = {'(': ')', '[': ']', '{': '}'}
    close_seq = {')': '(', ']': '[', '}': '{'}
    if seq == '':
        return True
    if len(seq) % 2 == 1:
        return False
    stack = []
    for i in seq:
        if i not in open_seq or i not in close_seq:
            continue
        if i in open_seq:
            stack.append(i)
        elif i in close_seq and len(stack) == 0:
            return False
        elif i in close_seq and close_seq[i] != stack[-1]:
            return False
        else:
            stack.pop(-1)
    return len(stack) == 0


def main() -> None:
    sequence = input()
    print("YES" if is_braces_sequence_correct(sequence) else "NO")


if __name__ == "__main__":
    main()
