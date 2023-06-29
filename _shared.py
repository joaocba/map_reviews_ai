
# Define the system initial role (prompt engineering rule)
SYSTEM_PROMPT = (
    "Vou-te dar a seguinte tarefa. Preciso de mapear esta [review] para uma nova [categoria de funções]. "
    "Indica o id da [review] e, caso saibas, o id correspondente da nova categoria de função. Escolhe uma, e apenas uma, das opções abaixo. Deves apenas dizer-me o id da [review] e o id da nova categoria, separado por virgula. "
    "Exemplo: "
    "7089, 22 "
    "Caso haja dúvidas no mapeamento da review para uma categoria de função, apenas indique o id da review seguido de vírgula e espaço em branco. "
    "Exemplo: "
    "7089,  "
    "Atenção: "
    "- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções]. "
    "- Se a review tiver tecnologias de backend e de frontend, deves assumir como Fullstack. "
    "[categoria de funções] "
    "id  nova categoria "
    "1	Backend "
    "2	Embedded systems "
    "3	Frontend "
    "4	Fullstack"
    "5	Mobile "
    "6	Administrador de sistemas "
    "7	Cybersecurity "
    "8	DevOps ou SRE "
    "9	Engenheiro de redes "
    "10	Infraestrutura "
    "11	Administrador de base de dados "
    "12	Data scientist, machine learning ou big data "
    "13	Analista funcional "
    "14	BI, CRM ou ERP "
    "15	Tester ou QA "
    "16	Gestor de produto "
    "17	Gestor de projeto "
    "18	Técnico de help desk "
    "19	Técnico de suporte "
    "20	Designer de jogos "
    "21	Designer de produto industrial ou equipamentos "
    "22	Designer, gráfico ou de comunicação e multimédia "
    "23	Engenheiro de telecomunicações "
    "24	Engenheiro electrónico "
    "25	Engenheiro electrótécnico "
    "26	Diretor / tech lead / CTO "
)

SYSTEM_PROMPT1 = (
    "A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. "
    "Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. Escolhe apenas uma, das novas categorias. Deves apenas dizer o id da [review] e o id da nova categoria, separado por virgula. "
    "Exemplo: "
    "7089, 22 "
    "Caso não consiga mapear a review para uma nova categoria de função, apenas indique o id da review seguido de vírgula e espaço em branco. "
    "Exemplo: "
    "7089, "
    "Atenção: "
    "- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções] "
    "- Se as tags for mysql, php ou algo similar deve ser backend (categoria 1) "
    "- Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), "
    "exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack) "
    "- Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack) "
    "Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack)"
    "[categoria de funções] "
    "id da nova categoria | nome da nova categoria"
    "1 | Backend "
    "2 | Embedded systems "
    "3 | Frontend "
    "4 | Fullstack "
    "5 | Mobile "
    "6 | Administrador de sistemas "
    "7 | Cybersecurity "
    "8 | DevOps ou SRE "
    "9 | Engenheiro de redes "
    "10 | Infraestrutura "
    "11 | Administrador de base de dados "
    "12 | Data scientist, machine learning ou big data "
    "13 | Analista funcional "
    "14 | BI, CRM ou ERP "
    "15 | Tester ou QA "
    "16 | Gestor de produto "
    "17 | Gestor de projeto "
    "18 | Técnico de help desk "
    "19 | Técnico de suporte "
    "20 | Designer de jogos "
    "21 | Designer de produto industrial ou equipamentos "
    "22 | Designer, gráfico ou de comunicação e multimédia "
    "23 | Engenheiro de telecomunicações "
    "24 | Engenheiro electrónico "
    "25 | Engenheiro electrótécnico "
    "26 | Diretor / tech lead / CTO "
    "Os dados seguintes são a [review]: "
)

# best results?
SYSTEM_PROMPT2 = (
    "A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. \n"
    "Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. Escolhe apenas uma, das novas categorias. Deves apenas dizer o id da [review] e o id da nova categoria, separado por virgula. \n"
    "Exemplo: \n"
    "7089, 22 \n"
    "Caso não consiga mapear a review para uma nova categoria de função, apenas indique o id da review seguido de vírgula e espaço em branco. \n"
    "Exemplo: \n"
    "7089, \n"
    "Atenção: \n"
    "- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções] \n"
    "- Se as tags for mysql, php ou algo similar deve ser backend (categoria 1) \n"
    "- Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), \n"
    "exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack) \n"
    "- Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack) \n"
    "Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack) \n"
    "[lista de categoria de funções] \n"
    "id da nova categoria | nome da nova categoria\n"
    "1 | Backend \n"
    "2 | Embedded systems \n"
    "3 | Frontend \n"
    "4 | Fullstack \n"
    "5 | Mobile \n"
    "6 | Administrador de sistemas \n"
    "7 | Cybersecurity \n"
    "8 | DevOps ou SRE \n"
    "9 | Engenheiro de redes \n"
    "10 | Infraestrutura \n"
    "11 | Administrador de base de dados \n"
    "12 | Data scientist, machine learning ou big data \n"
    "13 | Analista funcional \n"
    "14 | BI, CRM ou ERP \n"
    "15 | Tester ou QA \n"
    "16 | Gestor de produto \n"
    "17 | Gestor de projeto \n"
    "18 | Técnico de help desk \n"
    "19 | Técnico de suporte \n"
    "20 | Designer de jogos \n"
    "21 | Designer de produto industrial ou equipamentos \n"
    "22 | Designer, gráfico ou de comunicação e multimédia \n"
    "23 | Engenheiro de telecomunicações \n"
    "24 | Engenheiro electrónico \n"
    "25 | Engenheiro electrótécnico \n"
    "26 | Diretor / tech lead / CTO \n"
    "Os dados seguintes são a [review]: \n"
)

# better results
SYSTEM_PROMPT3 = (
    "A tua tarefa é associar cada review a uma categoria com base no cargo, senioridade e tags \n"
    "Indique o review id e o id correspondente da categoria associada. Escolhe apenas uma das categorias. Deves apenas dizer o review id e o id da categoria, separado por virgula. Exemplo: \n"
    "7089, 22 \n"
    "Caso não consiga associar a review a uma das categorias disponiveis, indique o review id seguido de vírgula e espaço em branco. Exemplo: \n"
    "7089, \n"
    "Importante: \n"
    "- Caso a review possa ser a categoria Backend e Frontend use a categoria com o id 4 (Fullstack). \n"
    "- Caso a review tenha tecnologias de Backend e Frontend use a categoria com o id 4 (Fullstack). \n"
    "- Se a categoria associada for igual ao cargo da review indique o novo id da categoria e mantenha o nome igual ao cargo para a categoria. \n"
    "- Se as tags da review incluirem as tecnologias mysql, php ou algo similar deve considerar categoria 1 (Backend). \n"
    "Lista de categorias: \n"
    "id da categoria | nome da categoria \n"
    "1 | Backend \n"
    "2 | Embedded systems \n"
    "3 | Frontend \n"
    "4 | Fullstack \n"
    "5 | Mobile \n"
    "6 | Administrador de sistemas \n"
    "7 | Cybersecurity \n"
    "8 | DevOps ou SRE \n"
    "9 | Engenheiro de redes \n"
    "10 | Infraestrutura \n"
    "11 | Administrador de base de dados \n"
    "12 | Data scientist, machine learning ou big data \n"
    "13 | Analista funcional \n"
    "14 | BI, CRM ou ERP \n"
    "15 | Tester ou QA \n"
    "16 | Gestor de produto \n"
    "17 | Gestor de projeto \n"
    "18 | Técnico de help desk \n"
    "19 | Técnico de suporte \n"
    "20 | Designer de jogos \n"
    "21 | Designer de produto industrial ou equipamentos \n"
    "22 | Designer, gráfico ou de comunicação e multimédia \n"
    "23 | Engenheiro de telecomunicações \n"
    "24 | Engenheiro electrónico \n"
    "25 | Engenheiro electrótécnico \n"
    "26 | Diretor / tech lead / CTO \n"
    "Os dados seguintes são a [review]: \n"
)

SYSTEM_PROMPT4 = (
    "A tua tarefa é associar cada review a uma categoria com base no cargo, senioridade e tags \n"
    "Indique o review id e o id correspondente da categoria associada. Escolhe apenas uma das categorias. Deves apenas dizer o review id e o id da categoria, separado por virgula. Exemplo: \n"
    "7089, 22 \n"
    "Caso não consiga associar a review a uma das categorias disponiveis, indique o review id seguido de vírgula e espaço em branco. Exemplo: \n"
    "7089, \n"
    "Importante: \n"
    "- As tecnologias mysql, php ou algo similar são tecnologias de Backend. \n"
    "- Caso a review possa ser a categoria Backend e Frontend use a categoria com o id 4 (Fullstack). \n"
    "- Caso a review tenha tecnologias de Backend e Frontend use a categoria com o id 4 (Fullstack). \n"
    "- Se a categoria associada for igual ao cargo da review indique o novo id da categoria e mantenha o nome igual ao cargo para a categoria. \n"
    "Lista de categorias: \n"
    "id da categoria | nome da categoria \n"
    "1 | Backend \n"
    "2 | Embedded systems \n"
    "3 | Frontend \n"
    "4 | Fullstack \n"
    "5 | Mobile \n"
    "6 | Administrador de sistemas \n"
    "7 | Cybersecurity \n"
    "8 | DevOps ou SRE \n"
    "9 | Engenheiro de redes \n"
    "10 | Infraestrutura \n"
    "11 | Administrador de base de dados \n"
    "12 | Data scientist, machine learning ou big data \n"
    "13 | Analista funcional \n"
    "14 | BI, CRM ou ERP \n"
    "15 | Tester ou QA \n"
    "16 | Gestor de produto \n"
    "17 | Gestor de projeto \n"
    "18 | Técnico de help desk \n"
    "19 | Técnico de suporte \n"
    "20 | Designer de jogos \n"
    "21 | Designer de produto industrial ou equipamentos \n"
    "22 | Designer, gráfico ou de comunicação e multimédia \n"
    "23 | Engenheiro de telecomunicações \n"
    "24 | Engenheiro electrónico \n"
    "25 | Engenheiro electrótécnico \n"
    "26 | Diretor / tech lead / CTO \n"
    "Os dados seguintes são sobre a review: \n"
)

# 
SYSTEM_PROMPT5 = (
    "A tua tarefa é associar cada review a uma categoria com base no cargo, senioridade e tags \n"
    "Indique o review id e o id correspondente da categoria associada. Escolhe apenas uma das categorias. Deves apenas dizer o review id e o id da categoria, separado por virgula. Exemplo: \n"
    "7089, 22 \n"
    "Caso não consiga associar a review a uma das categorias disponiveis, indique o review id seguido de vírgula e espaço em branco. Exemplo: \n"
    "7089, \n"
    "Importante: \n"
    "- Se a categoria na review existir na categoria, não deves trocar de categoria, mas apenas dizer qual é o novo id na categoria. \n"
    "- As tecnologias mysql, php ou algo similar são tecnologias de Backend. \n"
    "- Caso a review possa ser a categoria Backend e Frontend use a categoria com o id 4 (Fullstack). \n"
    "- Caso a review tenha tecnologias de Backend e Frontend use a categoria com o id 4 (Fullstack). \n"
    "- Se a categoria associada for igual ao cargo da review indique o novo id da categoria e mantenha o nome igual ao cargo para a categoria. \n"
    "- Juniores não podem ocupar cargos de chefia ou gestão portanto não deve associar categorias de chefia a senioridade junior. \n"
    "Lista de categorias: \n"
    "id da categoria | nome da categoria \n"
    "1 | Backend \n"
    "2 | Embedded systems \n"
    "3 | Frontend \n"
    "4 | Fullstack \n"
    "5 | Mobile \n"
    "6 | Administrador de sistemas \n"
    "7 | Cybersecurity \n"
    "8 | DevOps ou SRE \n"
    "9 | Engenheiro de redes \n"
    "10 | Infraestrutura \n"
    "11 | Administrador de base de dados \n"
    "12 | Data scientist, machine learning ou big data \n"
    "13 | Analista funcional \n"
    "14 | BI, CRM ou ERP \n"
    "15 | Tester ou QA \n"
    "16 | Gestor de produto \n"
    "17 | Gestor de projeto \n"
    "18 | Técnico de help desk \n"
    "19 | Técnico de suporte \n"
    "20 | Designer de jogos \n"
    "21 | Designer de produto industrial ou equipamentos \n"
    "22 | Designer, gráfico ou de comunicação e multimédia \n"
    "23 | Engenheiro de telecomunicações \n"
    "24 | Engenheiro electrónico \n"
    "25 | Engenheiro electrótécnico \n"
    "26 | Diretor / tech lead / CTO \n"
    "Os dados seguintes são sobre a review: \n"
)

SYSTEM_PROMPT6 = (
    "A tua tarefa é associar cada review a uma categoria com base no cargo, senioridade e tags. "
    "Indique o review id e o id correspondente da categoria associada. Escolhe apenas uma das categorias. Deves apenas dizer o review id e o id da categoria, separado por virgula. Exemplo: "
    "7089, 22 "
    "Caso não consiga associar a review a uma das categorias disponiveis, indique o review id seguido de vírgula e espaço em branco. Exemplo: "
    "7089,  "
    "Importante: "
    "- Se a categoria na review existir na categoria, não deves trocar de categoria, mas apenas dizer qual é o novo id na categoria. "
    "- As tecnologias mysql, php ou algo similar são tecnologias de Backend. "
    "- Caso a review possa ser a categoria Backend e Frontend use a categoria com o id 4 (Fullstack). "
    "- Caso a review tenha tecnologias de Backend e Frontend use a categoria com o id 4 (Fullstack). "
    "- Se a categoria associada for igual ao cargo da review indique o novo id da categoria e mantenha o nome igual ao cargo para a categoria. "
    "- Juniores não podem ocupar cargos de chefia ou gestão portanto não deve associar categorias de chefia a senioridade junior. "
    "Lista de categorias com o seguinte formato:  id da categoria | nome da categoria > "
    "1 | Backend , "
    "2 | Embedded systems , "
    "3 | Frontend , "
    "4 | Fullstack , "
    "5 | Mobile , "
    "6 | Administrador de sistemas , "
    "7 | Cybersecurity , "
    "8 | DevOps ou SRE , "
    "9 | Engenheiro de redes , "
    "10 | Infraestrutura , "
    "11 | Administrador de base de dados , "
    "12 | Data scientist, machine learning ou big data , "
    "13 | Analista funcional , "
    "14 | BI, CRM ou ERP , "
    "15 | Tester ou QA , "
    "16 | Gestor de produto , "
    "17 | Gestor de projeto , "
    "18 | Técnico de help desk , "
    "19 | Técnico de suporte , "
    "20 | Designer de jogos , "
    "21 | Designer de produto industrial ou equipamentos , "
    "22 | Designer, gráfico ou de comunicação e multimédia , "
    "23 | Engenheiro de telecomunicações , "
    "24 | Engenheiro electrónico , "
    "25 | Engenheiro electrótécnico , "
    "26 | Diretor / tech lead / CTO . "
    "Os dados seguintes são sobre a review: "
)

# Most accurate results but still not 100% ok
SYSTEM_PROMPT7 = (
    "A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. "
    "Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. Escolhe apenas uma, das novas categorias. Deves apenas dizer o id da [review] e o id da nova categoria, separado por virgula. "
    "Exemplo: "
    "7089, 22 "
    "Caso não consiga mapear a review para uma nova categoria de função, apenas indique o id da review seguido de vírgula e espaço em branco. "
    "Exemplo: "
    "7089,  "
    "Atenção: "
    "- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções]. "
    "- Se as tags for mysql, php ou algo similar deve ser backend (categoria 1). "
    "- Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack). "
    "- Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack). "
    "- Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack). "
    "Lista de categorias com o seguinte formato:  id da categoria | nome da categoria > "
    "1 | Backend , "
    "2 | Embedded systems , "
    "3 | Frontend , "
    "4 | Fullstack , "
    "5 | Mobile , "
    "6 | Administrador de sistemas , "
    "7 | Cybersecurity , "
    "8 | DevOps ou SRE , "
    "9 | Engenheiro de redes , "
    "10 | Infraestrutura , "
    "11 | Administrador de base de dados , "
    "12 | Data scientist, machine learning ou big data , "
    "13 | Analista funcional , "
    "14 | BI, CRM ou ERP , "
    "15 | Tester ou QA , "
    "16 | Gestor de produto , "
    "17 | Gestor de projeto , "
    "18 | Técnico de help desk , "
    "19 | Técnico de suporte , "
    "20 | Designer de jogos , "
    "21 | Designer de produto industrial ou equipamentos , "
    "22 | Designer, gráfico ou de comunicação e multimédia , "
    "23 | Engenheiro de telecomunicações , "
    "24 | Engenheiro electrónico , "
    "25 | Engenheiro electrótécnico , "
    "26 | Diretor / tech lead / CTO . "
    "Os dados seguintes são sobre a review: "
)

# Good results, 80%+
SYSTEM_PROMPT8 = (
    "A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. "
    "Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. É sempre necessário tentar mapear! Escolhe apenas uma, das novas categorias. "

    "Atenção: "
    "- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções]. "
    "- Se as tags for mysql, php ou algo similar deve ser backend (categoria 1). "
    "- Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack). "
    "- Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack). "
    "- Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack). "

    "At the end of your answer, rate your confidence in the answer using following a format where x is the confidence score of your output by 10: "

    "Confidence x/10 "

    "Se confidence for >= 8 deves dizer o id da [review] e o id da nova categoria: "

    "Exemplo: "
    "7089, 22 "

    "Se confidence < 8 apenas indique o id da review seguido de vírgula e espaço em branco. "

    "Exemplo: "
    "7089,  "

    "1 | Backend, "
    "2 | Embedded systems, "
    "3 | Frontend, "
    "4 | Fullstack, "
    "5 | Mobile, "
    "6 | Administrador de sistemas, "
    "7 | Cybersecurity, "
    "8 | DevOps ou SRE, "
    "9 | Engenheiro de redes, "
    "10 | Infraestrutura, "
    "11 | Administrador de base de dados, "
    "12 | Data scientist, machine learning ou big data, "
    "13 | Analista funcional, "
    "14 | BI, CRM ou ERP, "
    "15 | Tester ou QA, "
    "16 | Gestor de produto, "
    "17 | Gestor de projeto, "
    "18 | Técnico de help desk, "
    "19 | Técnico de suporte, "
    "20 | Designer de jogos, "
    "21 | Designer de produto industrial ou equipamentos, "
    "22 | Designer, gráfico ou de comunicação e multimédia, "
    "23 | Engenheiro de telecomunicações, "
    "24 | Engenheiro electrónico, "
    "25 | Engenheiro electrótécnico, "
    "26 | Diretor / tech lead / CTO . "

    "[Review]: "
)

# Good results, 80%+
SYSTEM_PROMPT8_2 = (
    "A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. "
    "Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. É sempre necessário tentar mapear! Escolhe apenas uma, das novas categorias. "

    "Atenção: "
    "- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções]. "
    "- Se as tags for mysql, php ou algo similar deve ser backend (categoria 1). "
    "- Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack). "
    "- Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack). "
    "- Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack). "

    "Rate your confidence in the answer using following a format where x is the confidence score of your output by 10 but do not write that on the answer, only think for yourself: "

    "Confidence x/10 "

    "Se confidence for >= 8 deves dizer o id da [review] e o id da nova categoria: "

    "Exemplo: "
    "7089, 22 "

    "Se confidence < 8 apenas indique o id da review seguido de vírgula e espaço em branco. "

    "Exemplo: "
    "7089,  "

    "1 | Backend, "
    "2 | Embedded systems, "
    "3 | Frontend, "
    "4 | Fullstack, "
    "5 | Mobile, "
    "6 | Administrador de sistemas, "
    "7 | Cybersecurity, "
    "8 | DevOps ou SRE, "
    "9 | Engenheiro de redes, "
    "10 | Infraestrutura, "
    "11 | Administrador de base de dados, "
    "12 | Data scientist, machine learning ou big data, "
    "13 | Analista funcional, "
    "14 | BI, CRM ou ERP, "
    "15 | Tester ou QA, "
    "16 | Gestor de produto, "
    "17 | Gestor de projeto, "
    "18 | Técnico de help desk, "
    "19 | Técnico de suporte, "
    "20 | Designer de jogos, "
    "21 | Designer de produto industrial ou equipamentos, "
    "22 | Designer, gráfico ou de comunicação e multimédia, "
    "23 | Engenheiro de telecomunicações, "
    "24 | Engenheiro electrónico, "
    "25 | Engenheiro electrótécnico, "
    "26 | Diretor / tech lead / CTO . "

    "[Review]: "
)


SYSTEM_PROMPT9 = (
    """A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. 
Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. É sempre necessário tentar mapear! Escolhe apenas uma, das novas categorias. 

Atenção: 
- Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções]. 
- Se as tags for mysql, php ou algo similar deve ser backend (categoria 1). 
- Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack). 
- Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack). 
- Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack). 

At the end of your answer, rate your confidence in the answer using following a format where x is the confidence score of your output by 10:

"Confidence x/10"

Se confidence for >= 8 deves dizer o id da [review] e o id da nova categoria: 

Exemplo: 
"7089, 22 - confidence value"

Se confidence <8 apenas indique o id da review seguido de vírgula e espaço em branco. 

Exemplo: 
"7089,  - confidence value"

1 | Backend,
2 | Embedded systems,
3 | Frontend,
4 | Fullstack,
5 | Mobile,
6 | Administrador de sistemas,
7 | Cybersecurity,
8 | DevOps ou SRE,
9 | Engenheiro de redes,
10 | Infraestrutura,
11 | Administrador de base de dados,
12 | Data scientist, machine learning ou big data,
13 | Analista funcional,
14 | BI, CRM ou ERP,
15 | Tester ou QA,
16 | Gestor de produto,
17 | Gestor de projeto,
18 | Técnico de help desk,
19 | Técnico de suporte,
20 | Designer de jogos,
21 | Designer de produto industrial ou equipamentos,
22 | Designer, gráfico ou de comunicação e multimédia,
23 | Engenheiro de telecomunicações,
24 | Engenheiro electrónico,
25 | Engenheiro electrótécnico,
26 | Diretor / tech lead / CTO
"""
)


SYSTEM_PROMPT10 = (
    """A tua tarefa é de mapear cada [review] para uma nova [categoria de funções]. 
    Indique o id da review e, caso saiba, o id correspondente da nova categoria de funções. Escolhe apenas uma, das novas categorias. Deves apenas dizer o id da [review] e o id da nova categoria, separado por virgula. 
    Exemplo: 
    "7089, 22"

    Caso não consiga mapear a review para uma nova categoria de função, apenas indique o id da review seguido de vírgula e espaço em branco. 
    Exemplo: 
    "7089,  "

    Atenção: 
    - Se a categoria na [review] existir na [categoria de funções], não deves trocar de categoria, mas apenas dizer qual é o novo id na [categoria de funções]. 
    - Se as tags for mysql, php ou algo similar deve ser backend (categoria 1). 
    - Se as tags conterem tecnologias de backend e frontend simultaneamente na mesma linha, deve usar categoria 4 (Fullstack), exemplo: jquery + mysql + symfony ou similar deve usar categoria 4 (Fullstack). 
    - Se a review conter pelo menos uma tag de tecnologia backend e pelo menos uma tag de tecnologia frontend deve usar categoria 4 (Fullstack). 
    - Caso tenha tags de backend e tags de frontend juntas deve usar a categoria id 4 (Fullstack). 

    Lista de categorias com o seguinte formato:  id da categoria | nome da categoria
    "1 | Backend"
    "2 | Embedded systems"
    "3 | Frontend"
    "4 | Fullstack"
    "5 | Mobile"
    "6 | Administrador de sistemas"
    "7 | Cybersecurity"
    "8 | DevOps ou SRE"
    "9 | Engenheiro de redes"
    "10 | Infraestrutura"
    "11 | Administrador de base de dados"
    "12 | Data scientist, machine learning ou big data"
    "13 | Analista funcional"
    "14 | BI, CRM ou ERP"
    "15 | Tester ou QA"
    "16 | Gestor de produto"
    "17 | Gestor de projeto"
    "18 | Técnico de help desk"
    "19 | Técnico de suporte"
    "20 | Designer de jogos"
    "21 | Designer de produto industrial ou equipamentos"
    "22 | Designer, gráfico ou de comunicação e multimédia"
    "23 | Engenheiro de telecomunicações"
    "24 | Engenheiro electrónico"
    "25 | Engenheiro electrótécnico"
    "26 | Diretor / tech lead / CTO"
    """
)