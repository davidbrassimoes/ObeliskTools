# **Cutting Around** 
Corte e Costura de Audio e Video

## cutcut.py
Corta audio/video aleatoriamente. O utilizador pode escolher o tamanho mínimo e máximo dos novos ficheiros, em segundos.

## reunited.py
Junta todos os ficheiros audio/video que estiverem dentro duma pasta. A pasta deverá ter ficheiros de um só tipo (ex: .mp3)

### Processo
1. Ter os scripts (*cutcut.py* e *reunited.py*) dentro duma pasta
2. Criar uma pasta para os exports dentro desta
3. Colocar o ficheiro a cortar dentro da primeira pasta
4. Correr script *cutcut.py* com o comando: **python cutcut.py <fileToCut> <exportFolder> <min_length> <max_length>**

    ex: *python cutcut.py myfile.mp4 out 3 5*
        
        Neste caso, o ficheiro *myfile.mp4* foi cortado num numero aleatorio de fragmentos entre os 3 e os 5 segundos para a pasta **out**

5. Correr script *reunited.py* com o comando: **python reunited.py <exportFolder>**
    ex: *python reunited.py out*

        Neste caso, o ficheiro final (que se chama sempre output.<formato>) fica na pasta **out**


