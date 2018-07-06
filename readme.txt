Nesse EP será gerada uma spline exata (sem ruído) aleatória e então será
adicionado ruido aos seus valores, para assim recuperarmos eles novamente
utilizando os métodos vistos em aula. Para rodar o EP bastar rodar o comando
    'python ep1.py'
e ter na pasta o módulo splines.py.
Serão plotados, em um gráfico, uma spline original aleatória (com n = 10) junto
com os valores com ruído, e, em outro gráfico, a spline recuperada usando
as fórmulas.

Para a criação da spline recuperada, é usada uma spline auxiliar e temporária para obter os valores de cada beta j em cada instante de tempo.