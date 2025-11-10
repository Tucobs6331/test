Descricao:
    Fazer um programa que gerencie os projetos semi-automaticamente e possivelmente os coloque para analise, o programa pode usar o github para isso por ser multiplataforma, mesmo assim, seria necessario alguma forma de fazer ser multiplataforma.

    Nao planejo interfaces graficas para isso, seria uma complicacao desnecessaria.

Possibilidades:
 Pode ser programado em Python seria acessivel para todos sistemas com python instalado e possivelmente em dispositivos moveis usando emuladores de terminal

 Devido uso do Git nao seria necessario uso de APIs complexas, sendo a parte mais complexa a propria programacao e automacao para funcionar em segundo plano.

 Poderiamos usar a biblioteca subprocess do python para mandar os comandos e a Watchdog para detectar mudancas, sao simples e definitivamente eficientes.

Posiveis Melhorias:
 Analise Automatica de projetos novos usando agentes LLM: Dificil por terem APIs quase sempre pagas e dificuldade extra na programacao, talvez precisariamos usar json que nao seria vantajoso devido escrita manual em txt.

