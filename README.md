# **Ferramentas Digital Obelisk**

## cutcut.py

Corta audio/video aleatoriamente. O utilizador pode escolher o tamanho mínimo e máximo dos novos ficheiros, em segundos.

## cutcutcut.py

Semelhante ao cutcut.py mas afeta uma pasta inteira.

## reunited.py

Junta todos os ficheiros audio/video que estiverem dentro duma pasta. A pasta deverá ter ficheiros de um só tipo (ex: .mp3).

## rename.py

Altera o nome de todos os ficheiros de uma pasta para **(prefixo)\_(numero)** ex: test_00.txt, test_01.mov, etc.. (aceita extensões diferentes)

## renameasy.py

O mesmo que o rename.py mas pede os valores um a um na consola em vez de aceitar tudo como argumentos no comando

# **Processos**

## cutcut.py

1.  Ter os scripts (_cutcut.py_ e _reunited.py_) dentro duma pasta
2.  Criar uma pasta para os exports dentro desta
3.  Colocar o ficheiro a cortar dentro da primeira pasta
4.  Correr script _cutcut.py_ com o comando: **python cutcut.py <fileToCut> <exportFolder> <min_length> <max_length>**

    ex: _python cutcut.py myfile.mp4 out 3 5_

        Neste caso, o ficheiro *myfile.mp4* foi cortado num numero aleatorio de fragmentos entre os 3 e os 5 segundos para a pasta **out**

5.  Correr script _reunited.py_ com o comando: **python reunited.py <exportFolder>**
    ex: _python reunited.py out_

        Neste caso, o ficheiro final (que se chama sempre output.<formato>) fica na pasta **out**

### **Note**

Podem ser colocados caminhos locais completos no comando, ou seja, pode-se ir cortar um ficheiro que está dentro doutra pasta qualquer e exportá-lo para uma terceira pasta, sem nenhuma delas ter de estar na mesma pasta que os scripts
