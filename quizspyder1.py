# -*- coding: utf-8 -*-
import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd

# Título do aplicativo
st.set_page_config(page_title="Quiz: Escola Econômica", layout="centered")
st.title("Quiz: Identificação de Escola Econômica")
st.markdown("Para estudantes de economia. Responda às perguntas abaixo e descubra com qual escola você mais se identifica.")

# Perguntas e alternativas
perguntas = [
    {
        "texto": "1. Por que o desemprego persiste mesmo em economias que estão crescendo?",
        "opcoes": [
            ("Falhas de mercado, como rigidez de salários e contratos, impedem ajustes rápidos no emprego.", "Novo-keynesiana"),
            ("A falta de demanda efetiva e a incerteza levam ao desemprego crônico, mesmo com capacidade produtiva ociosa.", "Pós-keynesiana"),
            ("Intervenções estatais distorcem o mercado de trabalho e impedem que ele se ajuste naturalmente.", "Austríaca"),
            ("O desemprego decorre de desequilíbrios temporários; o mercado tende a se ajustar sozinho ao pleno emprego.", "Neoclássica"),
            ("O desemprego é funcional ao capitalismo, usado para pressionar salários e manter a taxa de lucro.", "Marxista"),
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
            ("A inflação é estrutural ao capitalismo e decorre da luta entre capital e trabalho; só pode ser contida com reforma profunda.", "Marxista"),
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
            ("São instrumentos de dominação e concentração de poder, alheios às necessidades sociais reais.", "Marxista"),
            ("Funcionam bem quando há estabilidade monetária e previsibilidade nas regras de política econômica.", "Monetarista")
        ]
    },
    {
        "texto": "4. Qual a política ideal para comércio internacional?",
        "opcoes": [
            ("O livre comércio deve ser incentivado amplamente, pois promove especialização eficiente e ganhos mútuos entre países.", "Neoclássica"),
            ("É necessário proteger indústrias estratégicas nacionais com políticas seletivas até que possam competir globalmente.", "Novo-keynesiana"),
            ("Deve haver controle de fluxos de capitais e comércio regulado para garantir soberania e estabilidade macroeconômica.", "Pós-keynesiana"),
            ("É preciso reduzir a dependência externa e priorizar a autossuficiência nacional, rompendo com o imperialismo econômico.", "Marxista"),
            ("Acordos bilaterais voluntários e eliminação de barreiras são suficientes para gerar prosperidade, sem dirigismo estatal.", "Austríaca"),
            ("A estabilidade do comércio depende da manutenção de taxas de câmbio previsíveis e política monetária prudente.", "Monetarista")
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
            ("Regulamentar o crédito e atuar como instrumento de estabilização contra crises inerentes ao capitalismo.", "Marxista")
        ]
    },
    {
        "texto": "6. Como explicar a desigualdade de renda?",
        "opcoes": [
            ("É consequência natural das diferenças de produtividade entre indivíduos em um mercado meritocrático.", "Neoclássica"),
            ("É resultado da exploração estrutural do trabalho e da apropriação da mais-valia pelo capital.", "Marxista"),
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
            ("Adotar políticas fiscais expansionistas e transferências de renda emergenciais para preservar a demanda.", "Novo-keynesiana"),
            ("Conter o crédito e reduzir a liquidez, evitando alimentar bolhas e riscos morais futuros.", "Monetarista"),
            ("Crises são parte do ciclo do capital, causadas pela queda tendencial da taxa de lucro e superacumulação.", "Marxista")
        ]
    },
    {
        "texto": "8. A desigualdade social prejudica o crescimento econômico?",
        "opcoes": [
            ("Sim, ela reduz a demanda agregada e limita o consumo das massas, travando o crescimento sustentado.", "Pós-keynesiana"),
            ("Sim, pois resulta da exploração do trabalho e da concentração de capital, o que gera crises recorrentes e instabilidade.", "Marxista"),
            ("Não necessariamente; a desigualdade pode incentivar esforço e inovação, gerando crescimento no longo prazo.", "Neoclássica"),
            ("Não, desde que decorra de trocas voluntárias em um mercado livre e sem coerção estatal.", "Austríaca"),
            ("Depende: se for causada por falhas de mercado, como monopólios e exclusão educacional, pode prejudicar a eficiência e o crescimento.", "Novo-keynesiana"),
            ("Sim, principalmente quando combinada com inflação, pois reduz o poder de compra e gera instabilidade econômica.", "Monetarista")
        ]
    }
]

pontuacoes = {
    "Novo-keynesiana": 0,
    "Pós-keynesiana": 0,
    "Neoclássica": 0,
    "Marxista": 0,
    "Austríaca": 0,
    "Monetarista": 0
}

respostas = []

# Exibição de perguntas
with st.form("quiz_form"):
    for i, pergunta in enumerate(perguntas):
        st.markdown(f"#### {pergunta['texto']}")
        opcoes = pergunta["opcoes"]
        random.shuffle(opcoes)
        escolha = st.radio("", [opcao[0] for opcao in opcoes], key=f"pergunta_{i}")
        respostas.append((escolha, opcoes))
    submitted = st.form_submit_button("Ver Resultado")

# Resultado
if submitted:
    for i, (resposta_texto, opcoes) in enumerate(respostas):
        for texto, escola in opcoes:
            if texto == resposta_texto:
                pontuacoes[escola] += 1

    escola_principal = max(pontuacoes, key=pontuacoes.get)

    descricoes = {
        "Novo-keynesiana": (
            "Combina ideias keynesianas com microfundamentos. Aceita que mercados podem falhar devido a rigidez de preços, "
            "poder de mercado e informação assimétrica. Defende intervenções seletivas do Estado para corrigir falhas de mercado "
            "e estabilizar a economia. Autores: Stiglitz, Mankiw, Krugman."
        ),
        "Pós-keynesiana": (
            "Ênfase na incerteza fundamental, instabilidade financeira endógena e papel da demanda agregada. Crítica a visão "
            "de equilíbrio geral neoclássica. Defende forte intervenção estatal, políticas de renda e controle de capitais. "
            "Autores: Keynes, Kalecki, Minsky."
        ),
        "Neoclássica": (
            "Baseada na racionalidade dos agentes e equilíbrio geral. Acredita na eficiência dos mercados e que intervenções "
            "estatais geram distorções. Foco em modelos matemáticos e otimização. Autores: Walras, Marshall, Friedman."
        ),
        "Marxista": (
            "Analisa a economia através da luta de classes e exploração do trabalho. Crítica estrutural ao capitalismo como "
            "sistema intrinsecamente instável e injusto. Defende a superação do capitalismo. Autores: Marx, Engels, Luxemburgo."
        ),
        "Austríaca": (
            "Foca no individualismo metodológico, processos de mercado e conhecimento disperso. Rejeita qualquer intervenção "
            "estatal e modelos matemáticos complexos. Ênfase no empreendedorismo e ordem espontânea. Autores: Mises, Hayek, Kirzner."
        ),
        "Monetarista": (
            "Destaca o papel da oferta monetária na economia. Defende regras monetárias estáveis em vez de políticas discricionárias. "
            "Cunhou a frase 'Inflação é sempre e em todo lugar um fenômeno monetário'. Autores: Friedman, Schwartz, Brunner."
        )
    }

    st.success(f"Você se identifica com: {escola_principal}")
    st.info(descricoes[escola_principal])

    df_resultado = pd.DataFrame.from_dict(pontuacoes, orient='index', columns=['Pontuação'])
    df_resultado = df_resultado.sort_values('Pontuação', ascending=True)

    st.bar_chart(df_resultado) 
