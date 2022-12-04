'''
숫자 -> 알파벳으로 매칭하면됨
'''
def solution(age):
    age_dict = {
        '0':'a'
        ,'1':'b'
        ,'2':'c'
        ,'3':'d'
        ,'4':'e'
        ,'5':'f'
        ,'6':'g'
        ,'7':'h'
        ,'8':'i'
        ,'9':'j'
    }
    answer =''
    for i in str(age):
        answer += age_dict[i]
    return answer

def solution(age):
    age_dict = ['a','b','c','d','e','f','g','h','i','j']
    answer =''
    for i in str(age):
        answer += age_dict[int(i)]
    return answer