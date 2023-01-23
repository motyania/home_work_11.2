import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        return data


def get_candidate(canditates, candidate_id):
    """возвращает одного кандидата по его id"""

    for candidate in canditates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(canditates, candidate_name):
    """возвращает кандидатов по имени"""

    list_of_candidate = []
    for candidate in canditates:
        if candidate['name'].lower().find(candidate_name.lower()) != -1:
            list_of_candidate.append(candidate)

    return list_of_candidate


def get_candidates_by_skill(canditates, skill_name):
    """возвращает кандидатов по навыку"""

    list_of_candidate = []
    for candidate in canditates:
        skills = candidate["skills"].split(", ")
        skills = [x.lower() for x in skills]
        if skill_name.lower() in skills:
            list_of_candidate.append(candidate)

    return list_of_candidate
