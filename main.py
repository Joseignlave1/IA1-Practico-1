"""
IA I Práctico I

Investigación del Dataset del Titanic

Preguntas:

1-¿De qué trata exactamente este dataset?
Este dataset trata de pasajeros del titanic, se divide en 2 grupos, train.csv y test.csv
train.csv va a ser el dataset que debemos de utilizar para entrenar a nuestro modelo, este contiene detalles de un subconjunto de pasajeros(891) en los cuales se revela si sobrevivieron o no al Titanic
test.csv contiene información similar, pero no revela si sobrevivieron o no.
2-¿Cuál es el objetivo de la competencia de Kaggle?
El objetivo de la competencia es utilizando machine learning, crear un modelo que prediga cuáles pasajeros sobrevivieron al titanic

3-¿Qué columnas/atributos contiene el dataset?
El data set contiene las siguientes columnas
survival	Survival	0 = No, 1 = Yes
pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
sex	Sex
Age	Age in years
sibsp	# of siblings / spouses aboard the Titanic
parch	# of parents / children aboard the Titanic
ticket	Ticket number
fare	Passenger fare
cabin	Cabin number
embarked	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton

4-¿Qué representa cada una?
survival = representa si el pasajero sobrevivió o no al Titanic - 0 = No, 1 = Yes
pclass = Clase de su boleto(de acá se puede inferir posición económica)
sex = sexo, entiendo que hombre o mujer
sibsp = número de hermanos / conyugues a bordo
parch = número de padres / hijos a bordo
ticket = numero de ticket
fare = tarifa del pasajero
cabin = número de cabina
embarked = puerta de embarque(C = Cherbourg, Q = Queenstown, S = Southampton)

5-¿Cuál es la variable objetivo?
Entiendo según estuve investigando que la variable objetivo es la variable que representa el resultado de lo que queremos predecir
Por lo tanto, como queremos predecir cuales pasajeros sobrevivieron o no al Titanic, en este caso nuestra variable objetivo sería survival
las demás variables serían PREDICTORAS O EXPLICATIVAS.

6- Notebooks públicos revisados:
https://www.kaggle.com/code/alexisbcook/titanic-tutorial
https://www.kaggle.com/code/yousefaymanatia/titanic-predictions

7-¿Qué factores crees que más influyeron en la supervivencia?
Considero que los factores que más influyeron en la supervivencia fueron el sexo y la puerta de embarque
ya que se pudo ver en los notebooks que mas de un 75% de mujeres sobrevivieron frente a un 18% de hombres y que la gran mayoría de supervivientes
provenían de la puerta de embarque S = Southampton

train_data[train_data["Survived"] == 1]["Embarked"].value_counts()
Embarked
S    217
C     93
Q     30
Name: count, dtype: int64
7-¿Qué desafíos de calidad de datos esperas encontrar?
Los desafíos de calidad que espero encontrar son:
Age = el hecho de que sea un decimal, aunque entiendo que se hace así por la edad de los menores de 1 año
Cabin = muchas son NaN
Ticket = formato inconsistente, algunas filas tienen números y strings, y otras solo strings.

8-¿Qué variables podrían estar correlacionadas?
Considero que las variables fare y pclass sin duda estan relacionadas
ya que la clase asignada esta correlacionada con el precio de tu boleto.
Entiendo que cabin con pclass también está relacionada, ya que supongo que solo los que pagaron primera clase tienen una cabina.

Preguntas FINALES:
¿Qué variables parecen más relacionadas con Survived?

Considero que las variables mas relacionadas con Survived basándonos en el mapa de calor de correlaciónes y en los otros gráficos son:

fare = podemos visualizar que a mayor tarifa tenia el pasajero, más probable era que sobreviviera.

sex = ya que podemos visualizar un mediante el notebook de https://www.kaggle.com/code/alexisbcook/titanic-tutorial, que mas de un 75% de mujeres sobrevivieron, frente a un 18% de hombres

la supervivencia.

¿Dónde hay más valores faltantes? ¿Cómo los imputarías?
Considero que hay más valores faltantes en la columna "cabin", ya que entiendo que solo los pasajeros de primera clase tenían una cabina asignada, una buena técnica para
imputarlos sería asignarle el valor de "None" a los registros que no tengan cabina.
¿Qué hipótesis probarías a continuación?

La hipótesis que probaría sería el hecho de que a mayor tarifa, mas probable es que el pasajero sobreviva, por lo que podemos inferir que el nivel socioeconómico de los pasajeros
está estrechamente relacionado, también probaría el hecho de que el hecho de que si eras mujer era mucho mas probable de que sobrevivieras,
investigando el porqué de este suceso, descubrí que en el titanic se aplicó una política de "women and children first", por lo que mujeres y niños tenían prioridad para ocupar los botes salvavidas, lo que explica la gran diferencia de porcentajes
"""
