# def reorderLogFiles(self, logs:list[str]) -> list[str]:
#     letters, digits = [], []
#     for log in logs:
#         if log.split()[1].isdigit():
#             digits.append(log)
#         else:
#             letters.append(log)

#     #이제 문자 로그는 letters에 모두 모였으므로 다음과 같이 정렬하면 됨

#     letters.sort(key=lambda x:(x.split()[1], x.split()[0]))
#     return letters + digits



# 다시
class Solution(object):
    def reorderLogFiles(self, logs):
        letter = []
        digit = []
        for i in logs:
            if(i.split()[1].isdigit()):
                digit.append(i)
            else:
                letter.append(i)
        letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit