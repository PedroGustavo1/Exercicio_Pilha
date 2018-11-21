class Pilha():
#===================Construtor======================

  def __init__(self):
    self.pilha = []

#=======Adciona Um Elemento ao Topo da Pilha========

  def Push(self):
    elemento = int(input("Digite o Elemento a Ser Adcionado: "))
    self.pilha.append(elemento)
    print("Sua Pilha Agora �",self.pilha)

#=======Retira Um Elemento do Topo da Pilha=========
  
  def Pop(self):
    if (len(self.pilha)==0):
      print("N�o H� Elementos na Sua Pilha!")
    else:  
      self.pilha.pop()
      print("Sua Pilha Agora �",self.pilha)

#==========Verifica se a Pilha est� Vazia============
  
  def IsEmpty(self):
    if len(self.pilha) == 0:
      print("Sua Pilha Esta Vazia")
    else:
      print("Sua Pilha Contem Elementos")

#===========Verifica o Topo da Pilha=================
  
  def Peek(self):
    topo = self.pilha[-1]
    print("O Topo da Pilha � o",topo)

  #========Verifica o Tamanho da Pilha===============  
  def Length(self):
    tamanho = (len(self.pilha))
    if tamanho >1:
      print("Sua Pilha Contem %d Elementos"%(tamanho))
    elif tamanho ==1:
      print("Sua Pilha Contem 1 Elemento!")
    else:
      print("Sua Pilha N�o Contem Nenhum Elemento!")

p = Pilha()
print(p.pilha)
