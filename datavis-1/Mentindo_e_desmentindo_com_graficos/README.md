## Mentindo (e desmentindo) com gráficos
Trabalho final da disciplina Datavis I com o objetivo de identificar técnicas de manipulação em visualizações de dados e saber como evitá-las.

### Mensagem enganosa: Anitta não "envolveu" os brasileiros.

A partir dos dados do Spotify Charts, produzi um gráfico para passar a mensagem de que a cantora Anitta, apesar do sucesso mundial recente e chegada ao #1 do Spotify Global, não fez tanto sucesso entre os brasileiros.

<img align="center" width="1000" height="1000" src="https://raw.githubusercontent.com/biamuniz/mjda_insper/main/datavis-1/Mentindo_e_desmentindo_com_graficos/vis1_mensagem_enganosa.png">

* O eixo não começa do zero. Isso passa uma ideia de maior distância entre os limites superiores das colunas (veja no [link](https://raw.githubusercontent.com/biamuniz/mjda_insper/main/datavis-1/Mentindo_e_desmentindo_com_graficos/vis2_mensagem_enganosa_eixo_corrigido.png) uma versão do gráfico enganoso, mas com um eixo Y que começa no zero)
* Textos tendenciosos: destaque para o "queridinha" e "não envolveu", descrições subjetivas que não refletem _honestamente_ os dados;
* Não há informações metodológicas: apesar de não ser uma manipulação, entender como foi feita a análise e a origem dos dados é importante para compreender o gráfico. Uma informação não colocada é que foi incluída as músicas próprias de cada artista (por exemplo, "Envolver" e "Boy's don't cry", da Anitta) e participações em faixas de outro artista (como a música "No chão novinha", do Pedro Sampaio ft. Anitta);
* Cor: vermelho é comumente usado como negação, parada (pensando em semáforo), alerta. Diferentemente do verde, que passa ideia de aceitação. Colocar a cantora Anitta em vermelho destaca como uma peça fora do top5.

### Versão mais honesta do gráfico:
<img align="center" src="https://raw.githubusercontent.com/biamuniz/mjda_insper/main/datavis-1/Mentindo_e_desmentindo_com_graficos/vis3_mais_honesto.png">


### Bônus: Gráfico honesto, mas _um pouco tendencioso_:
Pensando em uma mensagem mais guiada para o leitor, seria interessante destacar a cantora Anitta e mostrar seu crescente sucesso no Spotify, decorrente da música envolver. Abaixo, uma sugestão de visualização:
<img align="center" src="https://raw.githubusercontent.com/biamuniz/mjda_insper/main/datavis-1/Mentindo_e_desmentindo_com_graficos/vis4_honesto.png">

### Ferramentas utilizadas:
* **Coleta e análise dos dados**: [Google Sheets](https://docs.google.com/spreadsheets/d/1qvDOxWPRLMr_Ye_fKuf2w10fA1AHJ2ADcitPXFW57gA/edit?usp=sharing) e o CTRL+C e CTRL+V
* **Construção dos gráficos**: Usei o flourish para fazer as escalas e os gráficos "brutos", que foram exportados em SVG e customizados no [Figma](https://www.figma.com/file/EjeJxykLvrr61DxSkkhNE4/Datavis-I---Mentindo-e-desmentindo-com-gr%C3%A1ficos?node-id=0%3A1). Link para os gráficos no flourish: [Gráfico com mensagem enganosa](https://public.flourish.studio/visualisation/9245836/) e [gráfico mais honesto](https://public.flourish.studio/visualisation/9245752/)
