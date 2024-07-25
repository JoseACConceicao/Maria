#Importar algumas bibliotecas
import streamlit as st

#*********************************Início da APP*************************************************************

#Título:
st.title("Um dia na História")
#Saudação inicial
#st.write("Bem vinda, Maria!")
#Estabelecer o dia
st.header("3 de setembro")
st.write("O dia 3 de setembro é uma data histórica: foi no 246º dia do calendário gregoriano (247º em anos bissextos) que se deram vários acontecimentos históricos de grande relevo.")
#Estabelecer a categoria de acontecimentos
with st.sidebar:
    st.markdown("**Tipos de acontecimentos a visualizar:**")
    EventosHistóricos = st.toggle("Eventos Históricos")
    Nascimentos = st.toggle("Nascimentos")
    Mortes = st.toggle("Mortes")

#Eventos históricos:

if EventosHistóricos:
    st.subheader("Principais Eventos Históricos" , divider= "rainbow")
    #Estabelecer que épocas evidenciar
    with st.sidebar:
        st.markdown("**Por favor selecione as principais épocas a visualizar:**")
        SeculosAntesDeCristo = st.toggle("Séculos antes de Cristo (a.C.)")              #a.C.
        SeculoIaXI = st.toggle("Século I a século XI")                                  #I a XI
        SeculoXIIaXIX = st.toggle("Século XII a seculo XIX")                            #XII a XIX
        SeculoXX = st.toggle("Século XX")                                               #XX
        SeculoXXI = st.toggle("Século XXI")                                             #XXI
        TodasAsEpocas = st.toggle("Todas as épocas")                                    #Todas
    if SeculosAntesDeCristo:
        st.markdown("")
        st.subheader("36 a.C. :")
        st.markdown("Na *Batalha de Nauloco*, ***Marco Vipsânio Agripa***, almirante de ***Otávio***, derrota ***Sexto Pompeu***, filho de ***Pompeo***, terminando assim a resistência pompeana ao *Segundo Triunvirato*.")
        st.image("nauloco.jpg", caption="Batalha de Nauloco")
    if SeculoIaXI:
        st.subheader("301:")
        st.markdown("***San Marino***, um dos mais pequenos países do mundo, e a república mais antiga ainda existente, é fundada por *São Marino*.")
        st.image("sanmarino.jpg" , caption="Bandeira de San Marino")
        st.subheader("590:")
        st.markdown("O ***Papa Gregório I***, ou *São Gregório Magnum*, é eleito.")
        st.image("gregorio.jpg" , caption="Papa Gregório I")
        st.subheader("673:")
        st.markdown("O Rei ***Vamba*** dos *Visigodos* reprime uma revolta de ***Hilderico***, governador de *Nimes* e rival ao trono.")
        st.image("vamba.jpg" , caption="A coroação do Rei Vamba")
        st.subheader("863:")
        st.markdown("Maior vitória bizantina na ***Batlha de Lalacão*** contra uma ataque árabe.")
        st.image("lalacao.jpg" , caption="Batlha de Lalacão")
    if SeculoXIIaXIX:
        st.subheader("1189:")
        st.markdown("Coroação de ***Ricardo I*** de *Inglaterra*.")
        st.image("ricardo.jpg" , caption="Coroação de Ricardo I de Inglaterra")
        st.subheader("1260:")
        st.markdown("Os *mamelucos* derrotam os *mongóis* na ***Batalha de Ain Jalut*** na *Palestina*, marcando a sua primeira derrota decisiva e o ponto de máxima expansão do *Império Mongol*.")
        st.image("ainjalut.jpg" , caption="Batalha de Ain Jalut")
        st.subheader("1335:")
        st.markdown("No *Congresso de Visegrád*, ***Carlos I da Hungria*** media uma reconciliação entre dois monarcas vizinhos, ***João da Boêmia*** e ***Casemiro III da Polónia***.")
        st.image("carlosI.jpg" , caption="Carlos I")
        st.subheader("1384:")
        st.markdown("Levamtamento do ***Cerco de Lisboa*** devido, sobretudo, à *Peste Negra*, que assolava o exército castelhano.")
        st.image("lisboa.jpg" , caption="Cerco a Lisboa de 1384")
        st.subheader("1411:")
        st.markdown("É celebrado o ***Tratado de Selymbria*** entre o *Império Otomano* e a *República de Veneza*.")
        st.image("selymbria.jpg" , caption="Tratado de Selymbria")
        st.subheader("1650:")
        st.markdown("A vitória sobre os monarquistas, na ***Batalha de Dunbar*** abre o caminho para *Edinburgh* para o **Novo Exército Modelo** na *Terceira Guerra Civil Inglesa*.")
        st.image("dunbar.jpg" , caption="Batlha de Dunbar")
        st.subheader("1658:")
        st.markdown("Aquando da morte de ***Oliver Cromwell***, o seu filho, ***Richard Cromwell***, torna-se o *Lorde Protetor* de Inglaterra.")
        st.image("cromwell.jpg" , caption="Richard Cromwell")
        st.subheader("1666:")
        st.markdown("O *Royal Exchange* arde, no ***Grande Incêndio de Londres***.")
        st.image("incendio.jpg" , caption="O Grande Incêndio de Londres")
        st.subheader("1758:")
        st.markdown("*D. José I* escapa de uma tentativa de rgicídio, da qual resulta o ***Processo dos Távoras***.")
        st.image("tavoras.jpg" , caption="Execução pública dos Távoras")
        st.subheader("1759:")
        st.markdown("Expulsão dos ***jesuítas*** dos terristórios portugueses.")
        st.image("jesuitas.jpg")
        st.subheader("1783:")
        st.markdown("A ***Guerra da Independência dos Estados Unidos*** termina com a assinatura do *Tratado de Paris* pelos Estados Unidos e o Reino da Grã-Bretanha.")
        st.image("teaparty.jpg" , caption="Tea Party: o início da revolução americana")
        st.subheader("1843:")
        st.markdown("O rei ***Otto, da Grécia*** é forçado a conceder uma nova constituição após uma *revolta* em Atenas")
        st.image("otto.jpg" , caption="O rei Otto")
        st.subheader("1861:")
        st.markdown("")