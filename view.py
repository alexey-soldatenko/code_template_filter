from django.shortcuts import render

def main_page(request):
    code = '''def solution(A):
#100%
positive = [i for i in A if i > 0]
positive = list(set(positive))
positive.sort()
if len(positive) > 1:
    for i in range(len(positive)):
        if i == 0:
            if positive[i] > 1:
                return 1
            continue
        elif (positive[i] - positive[i-1]) > 1:
            return positive[i-1]+1
    return positive[-1]+1
else:
    if positive[0] > 1:
        return 1
    else:
        return positive[0]+1
return 1'''
    return render(request, 'main_page.html', {'code':code})