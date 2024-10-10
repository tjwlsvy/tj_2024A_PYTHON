
#  day23 > 2_결정트리.py
# 주제 : 여러 어종의 특성(Weight,Length,Diagonal,Height,Width)들을 바탕으로 어종명(Species) 예측 하기
# Species : 어종명 , Weight:무게 , Length:길이 , Diagonal:대각선길이 , Height:높이 , Width:너비


# [1] 데이터셋
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv')
print( data.head()) # 확인

# [2] 7:3 비율로 훈련용 과 테스트용으로 분리하기
from sklearn.model_selection import train_test_split

x = data[['Weight','Length','Diagonal','Height','Width']]
y = data['Species']

# [3] 결정트리 모델로 훈련용 데이터 피팅 하기
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# [4] 훈련된 모델 기반으로 테스트용 데이터 예측하고 예측 정확도 확인하기
# 출력예시] 개선 전 결정트리모델 정확도 : 0.624
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=156)
model.fit(x_train , y_train)

from sklearn.metrics import accuracy_score
# 예측
y_predict = model.predict(x_test)
accurcy = accuracy_score(y_test , y_predict)

# [5] 최적의 하이퍼파라미터 찾기 # params = { 'max_depth' : [2 ,6 ,10 ,14 ] , 'min_samples_split: [ 2 , 4 ,6 ,8  ]}
# 출력예시 ] 평균 정확도 : 0.xxxxxxxxxx , 최적 하이퍼파라미터 : {'max_depth' : xx , 'min_samples_split' : x}
from sklearn.model_selection import GridSearchCV
params = {
    'max_depth' : [ 2 , 6 , 10 ,14 ],
    'min_samples_split' : [ 2 , 4 ,6 ,8  ]
}
grid_cv = GridSearchCV(model, param_grid=params , scoring='accuracy' , cv=5 ,return_train_score=True )
grid_cv.fit(x_train , y_train)
cv_results_df = pd.DataFrame(grid_cv.cv_results_)
cv_results_df[['param_max_depth' , 'mean_test_score' , 'mean_train_score']]
print(f'최적 정확도 {grid_cv.best_score_} , 최적 하이퍼 {grid_cv.best_params_}')

# [6] 최적의 하이퍼 파라미터 기반으로 모델 개선후 테스트용 데이터 예측하고 예측 정확도 확인하기 # 시각화하기
# 출력예시] 개선 후 결정트리모델 정확도 : 0.xxxxxx
# 차트 시각화

# 예시] 개선된 모델 생성
model2 = DecisionTreeClassifier( max_depth=9 , min_samples_split=8 )
model2.fit( x_train , y_train ) # 개선된 모델로 다시 피팅
    # 개선된 모델로 다시 테스트
Y_predict2 = model2.predict( x_test )           # 예측
print(  accuracy_score( y_test , Y_predict2 ) ) # 예측 정확도 확인

import matplotlib.pyplot as plt
from sklearn import tree # 결정트리 시각화 모듈
tree.plot_tree( model2  , feature_names= ['Weight','Length','Diagonal','Height','Width']  , class_names= ['Bream','Roach','Whitefish','Parkki','Perch','Pike','Smelt'])
    # tree.plot_tree( 결정트리모델객체 ,  feature_names = [피처이름들] , class_names=[클래스레이블들]   )
plt.show()







