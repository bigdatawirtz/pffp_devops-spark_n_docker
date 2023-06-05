# pffp_devops-spark_n_docker
Spark sobre docker

Neste repositorio podes encontrar o código necesario para crear unha imaxe e despois un contedor Docker con Spark.

Tamén se inclúe un dataset con datos sobre seguros e código pySpark para realizar dous exercicios de monitorización.

O código desenvolveuse durante un Proxecto de Formación de profesorado de Formación Profesional relacionado coas tecnoloxías DevOps.

## Como utilizar este repositorio

### Descargar o código
Clonar o repositorio desde a terminal:
`git clone https://github.com/bigdatawirtz/pffp_devops-spark_n_docker.git`

### Crear a imaxe Docker
O ficheiro Dockerfile contén as instrución para a creación da imaxe. Crear a imaxe:
`docker build -t spark_n_docker .`

### Lanzar un contedor
Lanzar o contedor a partir da imaxe creada:
`docker run --rm -it -p 4040:4040 spark_n_docker`

### Executar o código pySpark
A execución interactiva do contedor mostrará a consola pySpark na que executar o código. Pódese escribir o código a executar ou pegalo directamente desde outros ficheiros.

```Python 3.9.1 (default, Feb  9 2021, 07:42:03) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
``` 

### Monitorizar a execución do código pySpark
É posible acceder á interface de monitorización de Spark apuntando, co navegador, ao enderezo: http://localhost:4040

