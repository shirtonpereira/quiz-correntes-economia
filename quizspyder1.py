# -*- coding: utf-8 -*-
import streamlit as st
import random
import pandas as pd
import plotly.express as px

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Quiz: Escolas Econômicas",
    page_icon="📊",
    layout="centered"
)

# ---------------- TÍTULO PRINCIPAL ----------------
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📊 Quiz: Identificação de Escola Econômica</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Para estudantes de economia. Responda às perguntas abaixo e descubra com qual escola você mais se identifica!</p>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("ℹ️ Sobre o Quiz")
st.sidebar.info(
    "Quiz para explorar diferentes correntes do pensamento econômico. "
    "As alternativas foram formuladas para mapear sua afinidade.\n\n"
    "Feito com ❤️ usando Streamlit."
)

# ---------------- PERGUNTAS E ALTERNATIVAS ----------------
perguntas = [
    {
        "texto": "1. Por que o desemprego persiste mesmo em economias que estão crescendo?",
        "opcoes": [
            ("Falhas de mercado, como rigidez de salários e contratos, impedem ajustes rápidos no emprego.", "Novo-keynesiana"),
            ("A falta de demanda efetiva e a incerteza levam ao desemprego crônico, mesmo com capacidade produtiva ociosa.", "Pós-keynesiana"),
            ("Intervenções estatais distorcem o mercado de trabalho e impedem que ele se ajuste naturalmente.", "Austríaca"),
            ("O desemprego decorre de desequilíbrios temporários; o mercado tende a se ajustar sozinho ao pleno emprego.", "Neoclássica"),
            ("É um problema sistêmico, resultante de instituições e normas que perpetuam a concentração de poder e a instabilidade.", "Institucionalista"),
            ("A má gestão da política monetária gera incerteza e inflação, desestimulando o emprego sustentável.", "Monetarista")
        ]
    },
    {
        "texto": "2. Qual a melhor forma de controlar a inflação?",
        "opcoes": [
            ("Reduzindo a oferta monetária e adotando disciplina fiscal rigorosa para evitar pressões inflacionárias.", "Monetarista"),
            ("Utilizando políticas de controle de preços e negociação de salários, integradas a um pacto econômico nacional.", "Pós-keynesiana"),
            ("Aplicando metas de inflação com flexibilidade para suavizar os ciclos econômicos, por meio da política monetária.", "Novo-keynesiana"),
            ("Confiando que o mercado irá se ajustar sozinho, desde que não haja intervenção estatal ou expansão monetária artificial.", "Austríaca"),
            ("Através da reforma de instituições que causam a instabilidade de preços e desorganizam o sistema de preços.", "Institucionalista"),
            ("Adotando regras monetárias fixas e previsíveis, garantindo credibilidade do banco central perante os agentes econômicos.", "Neoclássica")
        ]
    },
    {
        "texto": "3. Os mercados financeiros são eficientes?",
        "opcoes": [
            ("Sim, os preços de ativos refletem racionalmente todas as informações disponíveis, promovendo alocação ótima de recursos.", "Neoclássica"),
            ("Não, os mercados são frequentemente instáveis devido a bolhas especulativas e comportamento irracional de agentes.", "Pós-keynesiana"),
            ("São geralmente eficientes no longo prazo, mas sofrem com rigidez de preços e expectativas não racionais no curto prazo.", "Novo-keynesiana"),
            ("A eficiência dos mercados é corrompida principalmente pela interferência estatal, que impede ajustes espontâneos.", "Austríaca"),
            ("Sua eficiência depende das regras, normas e regulamentações (instituições) que os governam.", "Institucionalista"),
            ("Funcionam bem quando há estabilidade monetária e previsibilidade nas regras de política econômica.", "Monetarista")
        ]
    },
    {
        "texto": "4. Qual a política ideal para comércio internacional?",
        "opcoes": [
            ("O livre comércio deve ser incentivado amplamente, pois promove especialização eficiente e ganhos mútuos entre países.", "Neoclássica"),
            ("É necessário proteger indústrias estratégicas nacionais com políticas seletivas até que possam competir globalmente.", "Novo-keynesiana"),
            ("Deve haver controle de fluxos de capitais e comércio regulado para garantir soberania e estabilidade macroeconômica.", "Pós-keynesiana"),
            ("A estabilidade do comércio depende da manutenção de taxas de câmbio previsíveis e política monetária prudente.", "Monetarista"),
            ("Acordos bilaterais voluntários e eliminação de barreiras são suficientes para gerar prosperidade, sem dirigismo estatal.", "Austríaca"),
            ("É preciso estabelecer e fortalecer instituições supranacionais que garantam uma competição justa e evitem o protecionismo.", "Institucionalista")
        ]
    },
    {
        "texto": "5. Qual deve ser o principal objetivo do banco central?",
        "opcoes": [
            ("Garantir estabilidade de preços acima de tudo, adotando uma política monetária neutra e sem surpresas.", "Monetarista"),
            ("Promover pleno emprego, crescimento sustentável e estabilidade financeira, além de conter a inflação.", "Pós-keynesiana"),
            ("Controlar a inflação dentro de uma meta, mas com flexibilidade para acomodar choques e ajudar no emprego.", "Novo-keynesiana"),
            ("Manter a força da moeda nacional e zelar por fundamentos macroeconômicos sólidos com mínima intervenção.", "Neoclássica"),
            ("O banco central é desnecessário: o mercado deve coordenar a emissão e uso da moeda livremente.", "Austríaca"),
            ("Assegurar a estabilidade do sistema financeiro por meio de regulamentação prudente e supervisão contínua.", "Institucionalista")
        ]
    },
    {
        "texto": "6. Como explicar a desigualdade de renda?",
        "opcoes": [
            ("É consequência natural das diferenças de produtividade entre indivíduos em um mercado meritocrático.", "Neoclássica"),
            ("É resultado de instituições e estruturas de poder que perpetuam privilégios e acesso desigual a oportunidades.", "Institucionalista"),
            ("Deriva de assimetrias de acesso ao crédito, educação e oportunidades entre diferentes grupos sociais.", "Pós-keynesiana"),
            ("É gerada por políticas públicas intervencionistas que desorganizam os sinais de mercado.", "Austríaca"),
            ("Resulta de falhas de mercado, como externalidades e poder de mercado, que não são corrigidas espontaneamente.", "Novo-keynesiana"),
            ("É acentuada por políticas inflacionárias mal conduzidas, que corroem o poder de compra das camadas mais pobres.", "Monetarista")
        ]
    },
    {
        "texto": "7. Como lidar com crises financeiras profundas?",
        "opcoes": [
            ("Atuar rapidamente com resgates pontuais e regulação prudencial para restaurar a confiança do mercado.", "Novo-keynesiana"),
            ("Assumir o controle direto do sistema financeiro, nacionalizando bancos e expandindo o investimento público.", "Pós-keynesiana"),
            ("Permitir que empresas insolventes quebrem para evitar distorções e criar incentivos corretos no mercado.", "Austríaca"),
            ("Conter o crédito e reduzir a liquidez, evitando alimentar bolhas e riscos morais futuros.", "Monetarista"),
            ("Crises são causadas pela falta de instituições adequadas para gerenciar a inovação financeira e a incerteza.", "Institucionalista"),
            ("Adoção de políticas fiscais expansionistas e transferências de renda emergenciais para preservar a demanda.", "Novo-keynesiana")
        ]
    },
    {
        "texto": "8. A desigualdade social prejudica o crescimento econômico?",
        "opcoes": [
            ("Sim, pois reduz a demanda agregada e limita o consumo, o que trava o crescimento econômico sustentado.", "Pós-keynesiana"),
            ("Sim, pois resulta de instituições e estruturas de poder que perpetuam a concentração de capital.", "Institucionalista"),
            ("Não necessariamente; a desigualdade pode incentivar o esforço e a inovação, gerando crescimento a longo prazo.", "Neoclássica"),
            ("Não, desde que decorra de trocas voluntárias em um mercado livre e sem coerção estatal.", "Austríaca"),
            ("Depende: se for causada por falhas de mercado, como monopólios e exclusão educacional, pode prejudicar a eficiência e o crescimento.", "Novo-keynesiana"),
            ("Sim, principalmente quando combinada com inflação, pois reduz o poder de compra e gera instabilidade econômica.", "Monetarista")
        ]
    },
    {
        "texto": "9. Qual o papel ideal do governo na economia?",
        "opcoes": [
            ("O papel deve ser o mínimo possível, limitado à garantia da lei, da ordem e dos direitos de propriedade.", "Austríaca"),
            ("O governo deve atuar para criar e reformar instituições que corrijam falhas e promovam um sistema mais justo e eficiente.", "Institucionalista"),
            ("O governo deve agir de forma ativa, usando a política fiscal e o gasto público para garantir o pleno emprego e a demanda agregada.", "Pós-keynesiana"),
            ("O papel principal do governo é prover bens públicos e regular mercados para corrigir falhas, sem interferir no sistema de preços.", "Neoclássica"),
            ("O governo deve ser disciplinado fiscalmente e atuar apenas para controlar a oferta de moeda, garantindo a estabilidade de preços.", "Monetarista"),
            ("O governo deve intervir de forma anticíclica, usando política monetária para estabilizar a economia diante de choques e rigidez.", "Novo-keynesiana")
        ]
    }
]

# ---------------- PONTUAÇÕES / ESTADO ----------------
# Inicializa o estado da sessão para armazenar as respostas
if 'respostas_do_quiz' not in st.session_state:
    st.session_state.respostas_do_quiz = {}
if 'opcoes_embaralhadas' not in st.session_state:
    st.session_state.opcoes_embaralhadas = {}

# ---------------- FORMULÁRIO DO QUIZ ----------------
with st.form("quiz_form"):
    for i, pergunta in enumerate(perguntas):
        st.markdown(
            f"<h3 style='font-size:22px; margin-top:25px; color:#2C3E50;'>{pergunta['texto']}</h3>",
            unsafe_allow_html=True
        )
        
        # Embaralha as opções apenas uma vez e armazena no estado da sessão
        if f"pergunta_{i}" not in st.session_state.opcoes_embaralhadas:
            opcoes_embaralhadas = pergunta["opcoes"][:]
            random.shuffle(opcoes_embaralhadas)
            st.session_state.opcoes_embaralhadas[f"pergunta_{i}"] = opcoes_embaralhadas

        opcoes_exibidas = st.session_state.opcoes_embaralhadas[f"pergunta_{i}"]
        
        # Cria o radio button para a pergunta
        resposta_escolhida = st.radio(
            "", 
            [opcao[0] for opcao in opcoes_exibidas], 
            key=f"resposta_pergunta_{i}"
        )
        # Armazena a resposta no estado da sessão
        st.session_state.respostas_do_quiz[f"pergunta_{i}"] = resposta_escolhida
        
    submitted = st.form_submit_button("✅ Ver Resultado")

# ---------------- RESULTADO ----------------
if submitted:
    # Reinicializa as pontuações
    pontuacoes = {
        "Novo-keynesiana": 0,
        "Pós-keynesiana": 0,
        "Neoclássica": 0,
        "Institucionalista": 0,
        "Austríaca": 0,
        "Monetarista": 0
    }
    
    # Processa as respostas para pontuar
    for i, pergunta in enumerate(perguntas):
        opcoes_originais = st.session_state.opcoes_embaralhadas[f"pergunta_{i}"]
        resposta_escolhida_texto = st.session_state.respostas_do_quiz[f"pergunta_{i}"]
        
        for texto, escola in opcoes_originais:
            if texto == resposta_escolhida_texto:
                pontuacoes[escola] += 1
                break

    # Encontra a escola principal
    escola_principal = max(pontuacoes, key=pontuacoes.get)
    
    descricoes = {
        "Novo-keynesiana": "Combina ideias keynesianas com microfundamentos. Aceita que mercados podem falhar e defende intervenções seletivas do Estado para corrigir falhas e estabilizar a economia. Autores: Stiglitz, Mankiw, Krugman.",
        "Pós-keynesiana": "Ênfase na incerteza fundamental, instabilidade financeira endógena e papel da demanda agregada. Crítica a visão de equilíbrio geral neoclássica. Defende forte intervenção estatal e controle de capitais. Autores: Keynes, Kalecki, Minsky.",
        "Neoclássica": "Baseada na racionalidade dos agentes e equilíbrio geral. Acredita na eficiência dos mercados e que intervenções estatais geram distorções. Foco em modelos matemáticos e otimização. Autores: Walras, Marshall, Friedman.",
        "Institucionalista": "Foca no papel das instituições (regras, normas, costumes) que moldam o comportamento econômico e os resultados de mercado. O mercado não é 'natural', mas uma construção social e histórica. Autores: Veblen, Commons, Coase, North.",
        "Austríaca": "Foca no individualismo metodológico, processos de mercado e conhecimento disperso. Rejeita qualquer intervenção estatal. Ênfase no empreendedorismo e ordem espontânea. Autores: Mises, Hayek, Kirzner.",
        "Monetarista": "Destaca o papel da oferta monetária na economia. Defende regras monetárias estáveis em vez de políticas discricionárias. 'Inflação é sempre e em todo lugar um fenômeno monetário'. Autores: Friedman, Schwartz, Brunner."
    }

    st.success(f"🎉 Você se identifica mais com a **{escola_principal}**!")
    st.info(descricoes[escola_principal])
    
    # Cria o dataframe e o gráfico com Plotly
    df_resultado = pd.DataFrame.from_dict(pontuacoes, orient='index', columns=['Pontuação']).sort_values('Pontuação', ascending=False)

    fig = px.bar(
        df_resultado,
        x=df_resultado.index,
        y="Pontuação",
        text="Pontuação",
        title="Resultado por Escola Econômica",
        labels={'index': 'Escola Econômica', 'Pontuação': 'Pontuação'},
        color_discrete_sequence=['#4CAF50']
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title="", yaxis_title="Pontuação", uniformtext_minsize=12, uniformtext_mode='hide')
    st.plotly_chart(fig, use_container_width=True)

    # Botão para refazer o quiz
    if st.button("🔄 Refazer Quiz"):
        # Limpa o estado da sessão para reiniciar o quiz
        for key in ["respostas_do_quiz", "opcoes_embaralhadas"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()






