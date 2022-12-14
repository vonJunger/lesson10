import json

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_all():
    return load_candidates()

def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate

    return

def get_candidate_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill in candidate['skills'].lower().split(', '):
            candidates.append(candidate)

    return candidates


