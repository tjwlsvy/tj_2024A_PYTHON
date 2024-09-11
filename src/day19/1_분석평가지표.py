
'''

    - 회귀분석 : 변수들간의 인과 관계 파악 / 분석
        - 종속변수가 독립변수의 변화에 따라 어떻게 변화 하는지 예측
        - 통계학 , 머신러닝

    - 머신러닝 : 컴퓨터에 입력된 데이터에서 스스로 패턴을 찾아 학습하여 새로운 지식을 만들고 예측하는 통찰을 제공하는 분야
        - 프로세스 : 1. 데이터 수집 -> 2. 전처리 -> 3. 모델구축 및 학습 -> 4. 모델평가 -> 5. 예측
        - 회귀 분석 결과에 대한 평가 지표
            1. MAE [ Mean Absolute Error , 평균 절대 오차 ]
                - 예측값과 실제값 사이의 절대 차이를 구하고 평균 계산 하는 방식
                    1. 절대 차이 계산 : 예측값 과 실제 값 차이의 절대값
                        - 예를 들어 실제 값이 0.5 이고 예측값이 0 일때 0.5

                    2. 평균 계산 : 모든 절대 차이의 평균을 구한다.

            2. MSE [ Mean Squared Error , 평균 제곱 오차 ]
                - 모델의 예측 값과 차이를 제곱하여 평군을 구하는 방식
                    1. 오차계산 : 예측값과 실제 값의 차이 # 차이를 오차(error) 라고 부른다.
                        - 예를 들어 실제값이 3 이고 예측값이 2.5 이라면 오차는 3 - 2.5 = 0.5
                    2. 제곱 : 각 오차를 제곱하여 양수로 변환 # 제곱하는 이유 : 오차의 부호가 문제되지 않도록 하기 위해 # 오차에 더 큰 페널티를 주기 위함
                        - 예를 들어 오차가 2 일경우 제곱 오차는 4 , 오차가 0.5 일경우 제곱 오차는 0.25
                    3. 평균 계산 : 모든 제곱 오차의 평균을 구한다.
                        - 예를 들어 제곱 오차가 4 , 9 , 1 이라면 4 + 9 + 1 / 3 = 14/3 = 4.67
                - MSE가 작을수록 모델의 예측이 실제 값에 가까워 진다.
                - mean_squared_error() 라이브러리

            3. RMSE[ ROOT Mean Squared Error , 루트 평균 제곱 오차 ]
                - MSE 의 제곱근으로 계산하는 방식 # 원래 데이터의 단위와 동일한 단위를 가지므로 해석이 직관적이다.
                    1. MSE 계산
                    2. 제곱근 계산 : MSE의 제곱근을 구한다. # 오차의 단위가 원래 단위로 변환하는 과정이다.

                MSE 와 RMSE 의 차이점

            4. 결정계수[ R-Squared ]!!
                - 모델이 데이터의 변동성이 얼마나 잘 설명하는지 나타나는 방법 # 예측력이 얼마나 강력한지 측정 # 값은 0에서 1사이
                    1. 총 변동성( Total sum of Squared , SST )
                        데이터와 실제 값이 평균값과 얼마나 차이가 나는지 측정 계산

                    2. 잔차 변동성( Residoel sum of Squared , SSE )
                        모델의 예측 값과 실제 값 사이의 차이를 측정 계산

                    3. 설명된 변동성
                        모델이 설명할수 없는 변동성의 양을 측정 즉] SST 에서 SSE 빼서 계산

                - 1에 가까울수록 모델이 데이터를 잘 설명하고 있다. 예측하고 있다.
                - 0에 가까울수록 모델이 예측에 대한 설명력이 전혀 없다고 의미 갖는다.



'''

# [1] 평가 지표 MSE
실제값 = [ 3 , -0.5 , 2 , 7 ]
예측값 = [ 2.5 , 0.0 , 2 , 8 ]
# 계산
from sklearn.metrics import mean_squared_error # sklearn
MSE = mean_squared_error(실제값 , 예측값)
print(f'mse : {MSE}') # mse : 0.375
'''
    1. 오차계산 
        오차1 = 3 - 2.5 = 0.5
        오차2 = -0.5 - 0.0 = -0.5
        오차3 = 2 - 2 = 0
        오차4 = 7 - 8 = -1
    2. 제곱 오차 계산 : 각 오차에 제곱
        제곱 오차1 = 0.5    = 0.25  (0.5 * 0.5)
        제곱 오차2 = -0.5   = 0.25  (-0.5 * -0.5)
        제곱 오차3 = 0      = 0     ( 0 * 0 )
        제곱 오차4 = -1     = 1     ( -1 * 1 )
    3. MSE : 모든 제곱 오차의 평균
            0.25 + 0.25 + 0 + 1         1.5
    MSE = ------------------------ = ------- = 0.375
                    4                   4
'''

# [2] 평가 지표 RMSE
import numpy as np #수학적 공식 제공하는 라이브러리
# 2. 모델 평가 # .sqrt() : 제곱근 함수
RMSE = np.sqrt( MSE )
print(f'rmse : {RMSE}') # rmse : 0.6123724356957945
'''
    MSE 계산 결과 : 0.375
    1. MSE 의 제곱근 구한다.
        0.6123724356957945
    
    - MSE 와 RMSE
        - 모델의 성능을  평가하기 위해 사용되는 두가지 오차(잔차) 측정 지표
        - 오차가 작을수록 예측 모델의 성능이 좋다는 것을 의미한다.
        - 단위 : 
            MSE는 제곱 단위로 표현 , 원래 데이터 단위와 다르다.
            RMSE는 원래 데이터 단위와 동일 하므로 해석이 직관적 이다.
        - 해석 : 
            MSE는 오차의 제곱 평균으로 , 수학적 편리함 제공한다.
            RMSE는 예측 오차의 평균적인 크기를 원래 단위로 제공한다.

'''

# [3] 평가 지표 , 결정 계수
# 2. 모델평가
from sklearn.metrics import r2_score
R2 = r2_score( 실제값 , 예측값 )
print(f'결정계수 :{R2}') # 결정계수 :0.9486081370449679

'''
    1. 실제 값의 평균 계산 
        3 + -0.5 + 2 + 7
        ----------------    = 2.875 
                4
    2. SSE(잔차 변동성) 계산 , 잔차의 제곱 합    ( 예측값의 분산 )
        오차1 = 3 - 2.5 = 0.5         0.25
        오차2 = -0.5 - 0.0 = -0.5     0.25
        오차3 = 2 - 2 = 0             0
        오차4 = 7 - 8 = -1            1
                                    = 1.5
    3. SST( 총 변동성 ) 계산 , 차이의 제곱 합   ( 실제값의 분산 )
        변동1 = 3 - 2.875     = 0.125     0.0156
        변동2 = -0.5 - 2.875  = -3.375    11.3906
        변동3 = 2 - 2.875     = 0.875     0.7656
        변동4 = 7 - 2.875     = 4.125     17.0156
                                        = 29.1874
                                        
            SSE         1.5              
    R = 1 - --- = 1 - ------- = 1 - 0.0514 = 0.9486  
            SST       29.1874
'''

# [4] 평가 지표 , MAE
from sklearn.metrics import mean_absolute_error
MAE = mean_absolute_error( 실제값 , 예측값 )
print(f'nae : {MAE}') # nae : 0.5














