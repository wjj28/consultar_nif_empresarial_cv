# Consultar NIF Empresarial CV

## Descrição
Este projeto é uma aplicação web para consulta de NIFs (Número de Identificação Fiscal) de empresas em Cabo Verde. Através da interface, os usuários podem pesquisar empresas utilizando seu NIF ou nome, com suporte para busca parcial.

## Funcionalidades
- Consulta de NIFs empresariais.
- Busca por nome da empresa com suporte a busca parcial.
- Apresentação de resultados com paginação (15 resultados por vez).
- Exibição de informações detalhadas sobre cada empresa encontrada.

## Fonte de Dados
Os dados utilizados na aplicação são extraídos do site [Porton di Nos ilha](https://portondinosilhas.gov.cv/), que fornece informações sobre empresas em Cabo Verde.

## Tecnologias Utilizadas
- **Flask**: Micro framework em Python para desenvolvimento web.
- **Pandas**: Biblioteca Python para manipulação e análise de dados.
- **HTML/CSS**: Para a criação da interface do usuário.

## Pré-requisitos
Para rodar esta aplicação, você precisa ter:
- Python 3.x instalado.
- Dependências listadas em `requirements.txt`.

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/wjj28/consultar_nif_empresarial_cv.git
