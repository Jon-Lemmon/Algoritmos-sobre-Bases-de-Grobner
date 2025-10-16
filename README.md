# Algoritmos-sobre-Bases-de-Grobner

Este repositório é parte do projeto de iniciação científica intitulado Polinômios, Bases de Gröbner e Álgebra Computacional, feito com o apoio financeiro do CNPq e apresentado no SIA UFV 2025. Estão aqui códigos em Python desenvolvidos com base nos algoritmos estudados ao longo do projeto, com o auxílio da biblioteca SymPy.

## Conteúdo

Este repositório contém duas classes Python de mesmo nome e mesmos métodos: ```Buchberger.py``` e ```Buchbeasy.py```. O primeiro contém os códigos desenvolvidos pelo bolsista, na tentativa de reproduzir os algorítmos de Buchberger, que já são implementados na biblioteca SymPy. Por isso, o segundo contém o mesmo código, porém utilizando a implementação do SymPy, servindo de referência durante os testes dos algorítmos. Há também o arquivo ```CheatSheet.txt```, que resume alguns recursos do SymPy. Inicialmente foi usado como apoio para o bolsista, mas foi mantido para complementar os comentários dos códigos, servindo de apoio agora para quem quiser entendê-los. Por fim, há uma lista de dependências ```requirements.txt``` e um ```Makefile```.

## Como rodar (Linux):

O ```Makefile``` do projeto reúne comandos de terminais Linux (bash) que permitem executar os códigos. Antes de executá-los pela primeira vez, é preciso primeiro criar um ambiente virtual e instalar as dependências nele.

### 1. Criar ambiente virtual (venv)

```bash
make inicializar_ambiente
```

Isto cria um ambiente virtual contendo a biblioteca SymPy na versão correta. Este comando só é necessário uma vez após baixar o repositório.

### 2. Executar teste dos algoritmos

Existe um arquivo de teste pronto para ser executado que compara os resultados obtidos pelos algoritmos já implementados pela biblioteca SymPy e os algoritmos desenvolvidos pelo bolsista. Para ver seu resultado, basta executar:

```bash
make executar_teste
```

### 3. Uso livre dos algorítmos no terminal

Para realizar seus próprios testes, é possível simplesmente importar as classes desenvolvidas em um código Python, ou ainda, rodar um terminal para executar um comando de cada vez. Para este último caso, basta executar

```bash
make executar_terminal
```

e será aberto um terminal interativo Python com a biblioteca SymPy e a classe contendo os algoritmos do repositório.