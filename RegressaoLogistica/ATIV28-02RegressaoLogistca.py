from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris.data
y = iris.target

#dividir em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)

#normalizar dados de teste
scaler = StandardScaler()
X_train_scalled = scaler.fit_transform(X_train)
X_test_scalled = scaler.transform(X_test)

#instanciar modelo de regressao
model = LogisticRegression()
model.fit(X_train_scalled,y_train)

#previsao
prediction = model.predict(X_test_scalled)
acuracia = accuracy_score(y_test, prediction)

print('A acurácia do modelo é',acuracia)