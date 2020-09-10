import numpy as np

def apk(actual,predicted,k=4, default=0.0):
    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hit = 0.0

    for i,p in enumerate(predicted):
        # 점수를 부여하는 조건 
        # p in actual  / p not in predicted[:i]
        if p in actual and p not in predicted[:i]:
            num_hit += 1.0
        # 점수 합 / 그 만큼의 개수 = score
        # 예를들어 [1 0 0 1] 맞춘횟수라면 정확도는  [1/1 0 0 2/4 ]
            score += num_hit / (i + 1.0)
    
    # 정답값이 공백일 경우, 무조건 0.0을 반환
    if not actual:
        return default

    # 정답의 개수(len(actual))로 average precision을 구한다.
    # 실제 정답이 5개이고 실제 수가 7이면 5로 계산
    # [1/1 + 2/4] / 2
    return score / min(len(actual), k)


def mapk(actual, predicted, k=4, default = 0.0):
    # list of list 인 정답 값(actual) 예측값(predicted)에서 
    # Average Precision을 구했으면 이제는
    # 각 값(데이터) 별 평균을 계산한다.
    # import numpy as np
    return np.mean([apk(actual,predicted,k,default) for a,p in zip(actual, predicted)])


