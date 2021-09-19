# 신규 아이디 추천

def solution(new_id):
    new_id = new_id.lower()
    for i in new_id:
        if i in '~!@#$%^&*()=+[{]}:?,<>/':
            new_id = new_id.replace(i, '')
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    while new_id:
        if new_id[0] == '.':
            new_id = new_id.replace('.', '', 1)
        break
    while new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        break
    if not new_id:
        new_id = 'aaa'
    elif len(new_id) >= 16:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    elif len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id