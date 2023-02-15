def solution(text, ending):
    # print(text[-len(ending) :], ending)
    # #  True if last string matches
    # if text[-len(ending) :] == ending:
    #     return True
    # else:
    #     return False

    # return text.endswith(ending)
    # return text[-len(ending) :] == ending

    # : means from the end of the string
    return ending in text[-len(ending) :]


if __name__ == "__main__":
    assert solution("samurai", "ai") == True
    assert solution("ninja", "ja") == True
    assert solution("sumo", "omo") == False
