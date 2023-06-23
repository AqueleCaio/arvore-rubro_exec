
#   comandos
#   
#   (i)nserir recebe numero e nome do aluno
#   i
#   1 Nome Aluno
#   
#   (b) buscar recebe o numero do aluno
#   b
#   1
#   
#   deve imprimir 
#   
#   "1 nao encontrado"
#   
#   ou
#   
#   "Nome Aluno"
#   
#   (max) devolve o aluno com o maior numero de matricula e imprime o numero e o nome
#   "1 Nome Aluno"
#   
#   (min) devolve o aluno com o menor numero de matricula e imprime o numero e o nome
#   "1 Nome Aluno"
#   
#   (x) fecha o programa

    
class noh:
    def __init__(self, mat):
        self.mat = mat
        self.esq = None
        self.dir = None
        self.cor = True

def rotacionaEsquerda(y):
    x = y.dir
    y.dir = x.esq
    x.esq = y
    x.cor = y.cor
    y.cor = True
    return x


def rotacionaDireita(y):
    x = y.esq
    y.esq = x.dir
    x.dir = y
    x.cor = y.cor
    y.cor = True
    return x

def sobeVermelho(y):
    y.cor = True
    y.esq.cor = False
    y.dir.cor = False

def ehVermelho(y):
    if y == None:
        return False
    else:
        return y.cor

def ehNegro(y):
    if y == None:
        return True
    else:
        return y.cor == False


def insere_aux(raiz, mat, nome, sobrenome):
    if raiz == None:
        return noh(mat)
    elif mat < raiz.mat:
        raiz.esq = insere_aux(raiz.esq, mat, nome, sobrenome)
    elif mat > raiz.mat:
        raiz.dir = insere_aux(raiz.dir, mat, nome, sobrenome)
    else:
        #jah existe esse mat, ignorar
        return raiz

    if ehVermelho(raiz.dir) and ehNegro(raiz.esq):
        raiz = rotacionaEsquerda(raiz)
    if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
        raiz = rotacionaDireita(raiz)
    if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
        sobeVermelho(raiz)
    return raiz

def insere(raiz, mat, nome, sobrenome):
    raiz = insere_aux(raiz, mat, nome, sobrenome)
    raiz.cor = False
    return raiz

def busca(raiz, mat):
    if raiz == None:
        return raiz
    if mat < raiz.mat:
        return busca(raiz.esq, mat)
    if mat > raiz.mat:
        return busca(raiz.dir, mat)
    return raiz

def minimum(raiz):
        while raiz.esq != None:
            raiz = raiz.esq
        return raiz

    # find the raiz with the maximum key
def maximum(raiz):
        while raiz.dir != None:
            raiz = raiz.dir
        return raiz

if __name__ == "__main__":
    
    resp = input()
    dado = input()
    arvore = None
    lista_nomes = []
    
    dados = dado.split(' ')
    lista_nomes.append(dados)
    
    while resp != 'x':
        if resp == 'i':
            arvore = insere(arvore, dados[0], dados[1], dados[2])
            
        elif resp == 'b':
            arvore = busca(arvore, dado[0])
            
        elif resp == 'max':
            maximum(arvore)
            
        elif resp == 'min':
            minimum(arvore)
            
        resp = input()