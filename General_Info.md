En este proyecto, nuestro equipo debe aplicar el ya conocido problema de enrutamiento de vehículos o VRP. Este se balla en hallar un conjunto de rutas optimas de entrega, teniendo en cuenta un punto de reparto, la distancia entre cada punto y un numero especifico de vehículos. El algoritmo VRP, esta altamente relacionado con el algoritmo TSP (problema del agente viajero), ya que este se basa también en la búsqueda de una ruta optima con la diferencia que el algoritmo VRP cuenta con muchos más destinos a los cuales llegar. Teniendo esto en cuenta, nuestro equipo deberá aplicar este algoritmo para un caso real. Donde contaremos con un mapa distribuido rectangularmente que contará con: 
•	Entre 50 y 100 puntos de distribución (almacenes).
•	Entre 2500 y 5000 puntos de entrega.
•	Una cantidad ilimitada de vehículos.
•	Costo por tiempo y distancia por cada vehículo.

La aplicación de este algoritmo , en un caso tan complejo como este resulta muy útil ya que puede ayudar a crear planes administrativos o de transporte en sectores extractivos. Esto no solo nos motivara a aplicar los conocimientos desarrollados en el curso, sino también a buscar soluciones para soluciones reales que pueden ser de mucha utilidad en campos de gran relevancia para el desarrollo del país. Por los cual, los objetivos establecidos serán: 
•	Aplicar los conceptos y habilidades desarrolladas en el curso 
•	Solucionar una problemática de gran impacto satisfactoriamente 
•	Utilizar y analizar diversos algoritmos para solucionar el problema




#Conceptos Generales:#

Para el desarrollo de este proyecto, será necesario aplicar ciertos conceptos explicados en el curso. Los cuales detallaremos a continuación: 

Fuerza Bruta: Esta refiere a una técnica de búsqueda que consiste en enumerar todos los posibles candidatos para la solución de un problema. Utilizando, como su propio nombre lo indica, la fuerza bruta de nuestra computadora. Por ejemplo, en el problema de las 8 reinas trabajado en clase(se posicionan 8 reinas en el tablero ubicadas de tal manera que no puedan atacarse entre ellas), la técnica de la fuerza bruta comprobaría cada una de las posiciones posibles en este tablero. Algo que no resulta totalmente optimo ya que realizaría más de 4 millones de comprobaciones, por lo cual , la fuerza bruta puede ser un buen método para comenzar a encontrar una solución a cualquier problema, y a partir de este punto, encontrar métodos mucho más óptimos.

Backtracking: El backtracking es una técnica de búsqueda sistemática a través de todos los estados posibles. Esta técnica utiliza la recursividad como parte fundamental de su funcionamiento. Ya que, dado un determinado estado, se verifica si este cumple con los requerimientos dados, en caso no los cumpla, se continua con el siguiente caso, pero volviendo a aplicar el algoritmo, básicamente volviendo atrás (backtrack). 

BFS: BFS o búsqueda de anchura es un algoritmo de búsqueda utilizado para recorrer o buscar elementos en un grafo. Para comenzar, debemos escoger el nodo como el elemento raíz desde donde comenzaremos a aplicar este algoritmo. A partir de este punto se comienza a explorar todos los nodos adyacentes a este nodo raíz, hasta que finalmente se recorra todo el árbol. 

DFS: DFS o búsqueda de profundidad es un algoritmo de búsqueda utilizado para recorrer o buscar elementos de un grafo. Este algoritmo consiste en ir expandiendo todos los nodos que va localizando, cuando ya no encuentra mas nodos que visitar, regresa (utilizando Backtracking) y vuelve a realizar el algoritmo hasta haber visitado todos los nodos.

