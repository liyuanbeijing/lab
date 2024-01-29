# 通配符*匹配
# 使用状态机实现

def is_match(text, pattern) -> bool:
    state = 'S0'
    for char in text:
        if state == 'S0':
            if char == 'a':
                state = 'S1'
            else:
                return False  # Invalid transition
        elif state == 'S1':
            if char == 'a':
                pass  # Stay in S1
            elif char == 'b':
                state = 'S2'
            else:
                return False  # Invalid transition
        elif state == 'S2':
            return False  # Invalid transition
    return state == 'S2'  # Only accept if we end in S2